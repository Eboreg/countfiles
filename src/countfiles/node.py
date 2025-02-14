import os
from typing import List, Optional

from countfiles.prepared_node import PreparedNode
from countfiles.utils import SortBy


class Node:
    children: "List[Node]"
    parent: Optional[str] = None

    def __init__(self, root: str, files: List[str], dirs: List[str], root_fd: int, count_dirs: bool):
        self.root_size = sum(self.get_file_size(name, root_fd) for name in files)
        self.root_filecount = len(files)
        self.root_dircount = len(dirs)
        if len(root) > 1:
            self.root = root.rstrip("/")
        else:
            self.root = root
        self.basename = self.root.strip("/").split("/")[-1]
        self.children = []
        self.count_dirs = count_dirs
        parent = self.root[:-len(self.basename)]
        if len(parent) > 1:
            parent = parent.rstrip("/")
        if parent != self.root:
            self.parent = parent

    def __str__(self):
        return f"Node[root={self.root}, parent={self.parent}, basename={self.basename}]"

    @property
    def descendant_count(self) -> int:
        total = len(self.children)
        for child in self.children:
            total += child.descendant_count
        return total

    @property
    def filecount(self):
        fc = self.root_filecount + sum(c.filecount for c in self.children)
        if self.count_dirs:
            fc += self.root_dircount
        return fc

    @property
    def recursive_size(self):
        return self.root_size + sum(c.recursive_size for c in self.children)

    def get_file_size(self, name: str, root_fd: int):
        try:
            return os.stat(name, dir_fd=root_fd).st_size
        except FileNotFoundError:
            # Probably means a broken symlink
            return 0

    def is_parent_of(self, path: str):
        return "/".join(path.split("/")[:-1]) == self.root

    def prepare(
        self,
        depth: int = 0,
        max_depth: Optional[int] = None,
        min_filecount: Optional[int] = None,
        prefix: str = "",
        is_last_child: bool = False,
        sort_by: SortBy = SortBy.NAME,
        reverse: bool = False,
        show_sizes: bool = False,
    ) -> PreparedNode:
        children = self.sort_and_filter_children(
            sort_by=sort_by,
            reverse=reverse,
            min_filecount=min_filecount,
            max_depth=max_depth,
            depth=depth,
        )

        not_shown = 0
        if max_depth and max_depth == depth + 1:
            not_shown = self.descendant_count
        elif len(self.children) > len(children):
            not_shown = len(self.children) - len(children)

        if not depth:
            child_prefix = ""
        elif is_last_child:
            child_prefix = prefix + "    "
        else:
            child_prefix = prefix + "│   "

        return PreparedNode(
            node=self,
            is_root=depth == 0,
            prefix=prefix,
            is_last_child=is_last_child,
            not_shown=not_shown,
            show_sizes=show_sizes,
            children=[
                child.prepare(
                    max_depth=max_depth,
                    min_filecount=min_filecount,
                    prefix=child_prefix,
                    is_last_child=idx == len(children) - 1,
                    sort_by=sort_by,
                    reverse=reverse,
                    depth=depth + 1,
                    show_sizes=show_sizes,
                ) for idx, child in enumerate(children)
            ],
        )

    def sort_and_filter_children(
        self,
        sort_by: SortBy,
        reverse: bool,
        depth: int,
        min_filecount: Optional[int],
        max_depth: Optional[int] = None,
    ):
        def sort_func(child: "Node"):
            if sort_by == SortBy.NAME:
                return child.basename
            if sort_by == SortBy.FILECOUNT:
                return child.filecount
            if sort_by == SortBy.SIZE:
                return child.recursive_size
            raise ValueError("This should not be possible.")

        if max_depth is not None and max_depth <= depth + 1:
            return []

        children = self.children

        if min_filecount:
            children = [c for c in children if c.filecount >= min_filecount]

        return sorted(children, key=sort_func, reverse=reverse)
