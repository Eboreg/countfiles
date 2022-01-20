#!/usr/bin/env python3

import argparse
import os
from typing import List


class Node:
    children: "List[Node]"

    def __init__(self, path: str):
        self.path = path.rstrip("/")
        self.basename = self.path.split("/")[-1]
        self.filecount = 0
        self.children = []

        with os.scandir(self.path) as it:
            for entry in it:
                if entry.is_file():
                    self.filecount += 1
                elif entry.is_dir():
                    self.add_child(entry.path)

    def __repr__(self) -> str:
        return f"[{str(self.filecount).rjust(8)}]  {self.basename}"

    def add_child(self, path: str):
        child = Node(path)
        self.filecount += child.filecount
        self.children.append(child)

    def print(self, max_depth=None, min_filecount=None, depth=0, prefix="", is_last_child=False):
        if depth:
            print(prefix, end="")
            if is_last_child:
                print("└── ", end="")
            else:
                print("├── ", end="")

        print(self)

        if max_depth is None or max_depth > depth + 1:
            if not depth:
                child_prefix = ""
            elif is_last_child:
                child_prefix = prefix + "    "
            else:
                child_prefix = prefix + "│   "
            if min_filecount:
                children = [c for c in self.children if c.filecount >= min_filecount]
            else:
                children = self.children
            for idx, child in enumerate(children):
                child.print(max_depth, min_filecount, depth + 1, child_prefix, idx == len(children) - 1)


def cli():
    parser = argparse.ArgumentParser(description="Show accumulated number of files per directory.")

    parser.add_argument("path", type=str)
    parser.add_argument(
        "--max-depth", "-md", type=int,
        help="Iterate all the way, but only show directories down to this depth."
    )
    parser.add_argument(
        "--min-filecount", "-mfc", type=int,
        help="Iterate all the way, but only show directories with this number of files or more."
    )

    args = parser.parse_args()

    root = Node(args.path)
    root.print(max_depth=args.max_depth, min_filecount=args.min_filecount)


if __name__ == "__main__":
    cli()
