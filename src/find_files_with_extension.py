from argparse import ArgumentParser
from pathlib import Path


def gather_args():

    arg_parser = ArgumentParser(
        description="Recursively lists files with a given extension."
    )

    arg_parser.add_argument(
        "target_ext", help="The extension to target. Leading period is optional."
    )

    arg_parser.add_argument(
        "--search_dir",
        nargs="?",
        type=Path,
        default=Path("."),
        help="The directory to start in.",
    )

    arg_parser.add_argument(
        "--full_paths",
        action="store_true",
        help="If provided, the full paths will be printed. Otherwise, relative paths are printed.",
    )

    args = arg_parser.parse_args()

    if not args.target_ext.startswith("."):

        args.target_ext = f".{args.target_ext}"

    return args


if __name__ == "__main__":

    args = gather_args()

    for file in args.search_dir.glob(f"**/*{args.target_ext}"):

        if args.full_paths:

            print(file.absolute().__str__())

        else:

            print(file.__str__())
