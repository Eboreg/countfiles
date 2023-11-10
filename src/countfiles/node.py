import os

import colorama
from colorama import Fore, Style


class Node:
    children: "list[Node]"

    def __init__(self, path: str):
        self.path = path.rstrip("/")
        self.basename = self.path.split("/")[-1]
        self.filecount = 0
        self.children = []

        with os.scandir(self.path) as it:
            for entry in it:
                if entry.is_file():
                    self.filecount += 1
                elif entry.is_dir() and not entry.is_symlink():
                    self.add_child(entry.path)

    def __lt__(self, other):
        return isinstance(other, Node) and self.basename.lower() < other.basename.lower()

    def __repr__(self) -> str:
        return f"[{str(self.filecount).rjust(10)}]  {self.basename}"

    def add_child(self, path: str):
        child = Node(path)
        self.filecount += child.filecount
        self.children.append(child)

    def print(
        self,
        max_depth: int | None = None,
        min_filecount: int | None = None,
        depth: int = 0,
        prefix: str = "",
        is_last_child: bool = False,
        color: bool = True,
    ):
        if color and not depth:
            colorama.init()

        if depth:
            print(prefix, end="")
            if is_last_child:
                print("└── ", end="")
            else:
                print("├── ", end="")

        output = f"[{str(self.filecount).rjust(10)}]  "
        if color:
            output += Fore.LIGHTWHITE_EX + Style.BRIGHT
        output += self.basename

        if min_filecount:
            children = [c for c in self.children if c.filecount >= min_filecount]
        else:
            children = self.children

        if (max_depth and max_depth == depth + 1 and children) or len(self.children) > len(children):
            if color:
                output += Fore.LIGHTBLACK_EX + Style.NORMAL
            output += "*"

        if color:
            print(output + Style.RESET_ALL)
        else:
            print(output)

        if children and (max_depth is None or max_depth > depth + 1):
            if not depth:
                child_prefix = ""
            elif is_last_child:
                child_prefix = prefix + "    "
            else:
                child_prefix = prefix + "│   "
            for idx, child in enumerate(sorted(children)):
                child.print(
                    max_depth=max_depth,
                    min_filecount=min_filecount,
                    depth=depth + 1,
                    prefix=child_prefix,
                    is_last_child=idx == len(children) - 1,
                    color=color,
                )
