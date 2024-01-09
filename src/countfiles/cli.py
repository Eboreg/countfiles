import argparse

from countfiles import __version__
from countfiles.node import Node


def cli():
    parser = argparse.ArgumentParser(prog="countfiles", description="Show accumulated number of files per directory.")

    parser.add_argument("path", type=str, default=".", nargs="?")
    parser.add_argument(
        "--max-depth", "-d", type=int,
        help="Iterate all the way, but only show directories down to this depth."
    )
    parser.add_argument(
        "--min-filecount", "-m", type=int,
        help="Iterate all the way, but only show directories with this number of files or more."
    )
    parser.add_argument("--sizes", "-s", action="store_true", help="Also show the total size of every directory.")
    parser.add_argument("--count-dirs", "-c", action="store_true", help="Also include directories in the file counts.")
    parser.add_argument("--no-color", action="store_true")
    parser.add_argument("--version", "-V", action="version", version="%(prog)s " + __version__)

    args = parser.parse_args()

    root = Node(args.path, count_dirs=args.count_dirs, show_sizes=args.sizes)
    root.print(max_depth=args.max_depth, min_filecount=args.min_filecount, color=not args.no_color)

    if args.max_depth or args.min_filecount:
        print("")
        print("* = one or more immediate subdirectories have been omitted")


if __name__ == "__main__":
    cli()
