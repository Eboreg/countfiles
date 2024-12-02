import enum
import locale
import os

import colorama
from colorama import Fore, Style


class SortBy(enum.Enum):
    NAME = 1
    FILECOUNT = 2
    SIZE = 3


class Node:
    children: "list[Node]"
    print_color: bool = True

    def __init__(self, path: str, count_dirs: bool = False, show_sizes: bool = False):
        self.path = path.rstrip("/")
        self.basename = self.path.split("/")[-1]
        self.filecount = 0
        self.size = 0
        self.children = []
        self.show_sizes = show_sizes
        self.count_dirs = count_dirs

        with os.scandir(self.path) as it:
            for entry in it:
                if entry.is_file():
                    self.filecount += 1
                    if self.show_sizes:
                        self.size += entry.stat().st_size
                elif entry.is_dir():
                    if count_dirs:
                        self.filecount += 1
                    if not entry.is_symlink():
                        self.add_child(path=entry.path)

    def __lt__(self, other):
        return isinstance(other, Node) and self.basename.lower() < other.basename.lower()

    def __repr__(self) -> str:
        return f"[{str(self.filecount).rjust(10)}]  {self.basename}"

    def add_child(self, path: str):
        child = Node(path, count_dirs=self.count_dirs, show_sizes=self.show_sizes)
        self.filecount += child.filecount
        self.size += child.size
        self.children.append(child)

    def count_descendants(self) -> int:
        total = len(self.children)
        for child in self.children:
            total += child.count_descendants()
        return total

    def format_size(self) -> str:
        terabytes = round(self.size / 1024 / 1024 / 1024 / 1024, 1)
        if terabytes >= 1.0:
            return locale.str(terabytes) + "T"
        gigabytes = round(self.size / 1024 / 1024 / 1024, 1)
        if gigabytes >= 1.0:
            return locale.str(gigabytes) + "G"
        megabytes = round(self.size / 1024 / 1024, 1)
        if megabytes >= 1.0:
            return locale.str(megabytes) + "M"
        kilobytes = round(self.size / 1024, 1)
        if kilobytes >= 1.0:
            return locale.str(kilobytes) + "K"
        return str(self.size)

    def get_children(self, sort_by: SortBy, reverse: bool, min_filecount: int | None):
        def sort_func(child: Node):
            match sort_by:
                case SortBy.NAME:
                    return child.basename
                case SortBy.FILECOUNT:
                    return child.filecount
                case SortBy.SIZE:
                    return child.size

        children = self.children

        if min_filecount:
            children = [c for c in children if c.filecount >= min_filecount]

        return sorted(children, key=sort_func, reverse=reverse)

    def print_string(self, string: str = "", color: str = ""):
        if self.print_color and color:
            print(color, end="")
        print(string, end="")
        if self.print_color:
            print(Style.RESET_ALL, end="")

    def print(
        self,
        max_depth: int | None = None,
        min_filecount: int | None = None,
        depth: int = 0,
        prefix: str = "",
        is_last_child: bool = False,
        color: bool = True,
        sort_by: SortBy = SortBy.NAME,
        reverse: bool = False,
    ):
        self.print_color = color
        if color and not depth:
            colorama.init()

        if depth:
            self.print_string(prefix)
            if is_last_child:
                self.print_string("└── ")
            else:
                self.print_string("├── ")

        self.print_string(f"[{str(self.filecount).rjust(6)}")
        if self.show_sizes:
            self.print_string(f"; {self.format_size().rjust(6)}")
        self.print_string("]  ")

        self.print_string(self.basename, color=Fore.LIGHTWHITE_EX + Style.BRIGHT)

        children = self.get_children(sort_by=sort_by, reverse=reverse, min_filecount=min_filecount)

        not_shown = 0
        if max_depth and max_depth == depth + 1:
            not_shown = self.count_descendants()
        elif len(self.children) > len(children):
            not_shown = len(self.children) - len(children)
        if not_shown:
            if not_shown == 1:
                self.print_string(" (1 descendant directory not shown)", color=Fore.LIGHTBLACK_EX)
            else:
                self.print_string(f" ({not_shown} descendant directories not shown)", color=Fore.LIGHTBLACK_EX)

        self.print_string("\n")

        if children and (max_depth is None or max_depth > depth + 1):
            if not depth:
                child_prefix = ""
            elif is_last_child:
                child_prefix = prefix + "    "
            else:
                child_prefix = prefix + "│   "

            for idx, child in enumerate(children):
                child.print(
                    max_depth=max_depth,
                    min_filecount=min_filecount,
                    depth=depth + 1,
                    prefix=child_prefix,
                    is_last_child=idx == len(children) - 1,
                    color=color,
                    sort_by=sort_by,
                    reverse=reverse,
                )
