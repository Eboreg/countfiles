import math
import os
from typing import TYPE_CHECKING, Dict, List, Optional

import colorama

from countfiles.node import Node
from countfiles.utils import SortBy


if TYPE_CHECKING:
    from countfiles.prepared_node import PreparedNode


class Tree:
    _root: Node

    def __init__(
        self,
        path: str,
        count_dirs: bool = False,
        show_sizes: bool = False,
        max_depth: Optional[int] = None,
        min_filecount: Optional[int] = None,
        color: bool = True,
        sort_by: SortBy = SortBy.NAME,
        reverse: bool = False,
        symlinks: bool = False,
        hidden: bool = True,
    ):
        self.path = os.path.realpath(path)
        self.basename = path.rstrip("/").split("/")[-1]
        self.count_dirs = count_dirs
        self.show_sizes = show_sizes
        self.max_depth = max_depth
        self.min_filecount = min_filecount
        self.color = color
        self.sort_by = sort_by
        self.reverse = reverse
        self.symlinks = symlinks
        self.hidden = hidden

    def __str__(self):
        if self.color:
            colorama.init()

        prepared_root = self.root.prepare(
            max_depth=self.max_depth,
            min_filecount=self.min_filecount,
            sort_by=self.sort_by,
            reverse=self.reverse,
            show_sizes=self.show_sizes,
        )
        lines = prepared_root.output(columns=self.get_output_width(prepared_root))
        if self.color:
            return "\n".join(line.colored for line in lines)
        return "\n".join(line.text for line in lines)

    @property
    def root(self) -> Node:
        if hasattr(self, "_root"):
            return self._root

        nodes: Dict[str, Node] = {}
        seen_inodes: List[int] = []

        for root, dirs, files, root_fd in os.fwalk(self.path, follow_symlinks=self.symlinks):
            if not self.hidden:
                if root != self.path and os.path.basename(root).startswith("."):
                    continue
                files = [f for f in files if not f.startswith(".")]
                dirs = [d for d in dirs if not d.startswith(".")]

            if self.symlinks and os.path.islink(root):
                root_inode = os.lstat(root).st_ino
                if root_inode in seen_inodes:
                    raise RuntimeError(
                        f"Infinite recursion detected for symlink {root}; try again without --symlinks."
                    )

                seen_inodes.append(root_inode)
                target = os.path.realpath(os.path.join(os.path.dirname(root), os.readlink(root)))

                if target.startswith(self.path):
                    # Link target is already included in the selection and
                    # we don't want to count its contents twice:
                    continue

            node = Node(root=root, files=files, dirs=dirs, root_fd=root_fd, count_dirs=self.count_dirs)
            nodes[node.root] = node

            if not hasattr(self, "_root"):
                self._root = node
            if node.parent and node.parent in nodes:
                nodes[node.parent].children.append(node)

        return self._root

    def get_output_width(self, root: "PreparedNode"):
        try:
            max_width = os.get_terminal_size().columns
        except OSError:
            max_width = 80
        min_width = min(80, max_width)
        real_width = root.col1_width
        if real_width >= max_width:
            return max_width
        if real_width < min_width:
            return min_width
        return math.ceil(real_width / 10) * 10
