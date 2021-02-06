from argparse import ArgumentParser, RawTextHelpFormatter
from pathlib import Path

import colorama
from colorama import Fore, Back, Style


def print_file(do_print_full_path,file):

    if do_print_full_path:

        print(file.absolute().__str__())

    else:

        print(file.__str__())  

def yield_files_with_extension(target_dir,target_ext):

    for file in target_dir.glob(f"**/*{target_ext}"):

        if not file.is_dir():

            yield file

def collect_target_ext(args):

    target_ext = args.target_ext

    if not target_ext.startswith('.'):
        
        target_ext = '.' + target_ext

    return target_ext

def main(args):

    target_ext = collect_target_ext(args)

    for file in yield_files_with_extension(args.target_dir,target_ext):

        print_file(args.full_paths,file)

def print_banner():

    print(fr'''{Fore.GREEN}

 __   __     ______     __     __     ______  
/\ "-.\ \   /\  ___\   /\ \  _ \ \   /\__  _\ 
\ \ \-.  \  \ \  __\   \ \ \/ ".\ \  \/_/\ \/ 
 \ \_\\"\_\  \ \_____\  \ \__/".~\_\    \ \_\ 
  \/_/ \/_/   \/_____/   \/_/   \/_/     \/_/ 
                                              

{Fore.RESET}{Fore.YELLOW}fiNd filEs With exTension{Fore.RESET}''')

def gather_args():

    arg_parser = ArgumentParser(
        formatter_class=RawTextHelpFormatter,
        description="Recursively lists files with a given extension in a target directory.",
        prog="NEWT.exe",
        epilog=f'''==========================

{Fore.YELLOW}Usage Examples{Fore.RESET}

Searching for .py files in the current directory.

    {Fore.GREEN + Style.BRIGHT}NEWT.exe .py{Style.RESET_ALL}

Searching for .jpg files in a different directory.

    {Fore.GREEN + Style.BRIGHT}NEWT.exe .jpg path/to/target/search/dir{Style.RESET_ALL}

Searching for .mp3 files in this directory, printing the results as full paths.

    {Fore.GREEN + Style.BRIGHT}NEWT.exe .mp3 --full-paths{Style.RESET_ALL}
{Fore.RESET}'''
    )

    arg_parser.add_argument(
        "target_ext", help="The extension to list. Leading period is optional."
    )

    arg_parser.add_argument(
        "target_dir",
        nargs="?",
        type=Path,
        default=Path("."),
        help="The directory to search in.",
    )

    arg_parser.add_argument(
        "--full-paths",
        '-fp',
        action="store_true",
        help="If provided, the full paths will be printed. Otherwise, relative paths are printed.",
    )

    return arg_parser.parse_args()

if __name__ == "__main__":

    colorama.init()

    print_banner()

    args = gather_args()

    main(args)
