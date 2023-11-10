import argparse

from countfiles import __version__
from countfiles.node import Node


def cli():
    parser = argparse.ArgumentParser(prog="countfiles", description="Show accumulated number of files per directory.")

    parser.add_argument("path", type=str)
    parser.add_argument(
        "--max-depth", "-md", type=int,
        help="Iterate all the way, but only show directories down to this depth."
    )
    parser.add_argument(
        "--min-filecount", "-mfc", type=int,
        help="Iterate all the way, but only show directories with this number of files or more."
    )
    parser.add_argument("--no-color", action="store_true")
    parser.add_argument("--version", "-V", action="version", version="%(prog)s " + __version__)

    args = parser.parse_args()

    root = Node(args.path)
    root.print(max_depth=args.max_depth, min_filecount=args.min_filecount, color=not args.no_color)

    if args.max_depth or args.min_filecount:
        print("")
        print("* = one or more immediate subdirectories have been omitted")


if __name__ == "__main__":
    cli()
