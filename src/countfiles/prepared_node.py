from typing import TYPE_CHECKING, List

from colorama import Fore, Style

from countfiles.output_line import OutputLine
from countfiles.utils import format_size


if TYPE_CHECKING:
    from countfiles.node import Node


class PreparedNode:
    def __init__(
        self,
        node: "Node",
        is_root: bool,
        prefix: str,
        is_last_child: bool,
        not_shown: int,
        show_sizes: bool,
        children: "List[PreparedNode]",
    ):
        self.root_size = node.root_size
        self.recursive_size = node.recursive_size
        self.children = children
        self.node = node
        self.is_root = is_root
        self.prefix = prefix
        self.is_last_child = is_last_child
        self.col1_suffix = ""
        self.show_sizes = show_sizes

        if not_shown == 1:
            self.col1_suffix = " (1 child not shown)"
        elif not_shown > 1:
            self.col1_suffix = f" ({not_shown} children not shown)"

    @property
    def col1_width(self):
        result = 0
        if not self.is_root:
            result += len(self.prefix) + 4
        result += 10  # filecount
        result += len(self.node.basename)
        result += len(self.col1_suffix)
        if self.show_sizes:
            result += 16

        return max([result, *[c.col1_width for c in self.children]])

    def output(self, columns: int) -> List[OutputLine]:
        line = OutputLine()

        if not self.is_root:
            line.append(self.prefix)
            if self.is_last_child:
                line.append("└───")
            else:
                line.append("├───")

        line.append(f"[{str(self.node.filecount).rjust(6)}]  ")
        line.append(self.node.basename, color=Fore.LIGHTWHITE_EX + Style.BRIGHT)

        col1_width = columns - 16 - len(self.col1_suffix) if self.show_sizes else columns - len(self.col1_suffix)
        line = line.clone().truncate(col1_width)
        line.append(self.col1_suffix, color=Fore.LIGHTBLACK_EX)

        lines = [line]

        if self.show_sizes:
            remaining_columns = columns - line.length - 8
            root_size = (" " + format_size(self.root_size)).rjust(remaining_columns)
            recursive_size = " " + format_size(self.recursive_size).rjust(7)
            line.append(root_size)
            line.append(recursive_size, color=Fore.LIGHTWHITE_EX)

        for child in self.children:
            lines.extend(child.output(columns=columns))

        return lines
