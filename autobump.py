import argparse
import glob
import itertools
import shlex
from datetime import datetime


def bump(filepath: str):
    year = datetime.now().year
    with open(filepath) as file:
        content = file.read()
        content = content.replace(year - 1, year)
    with open(filepath, 'w') as file:
        file.write(content)


parser = argparse.ArgumentParser()
parser.add_argument('--glob', type=str, required=True)
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()

glob_paths = shlex.split(args.glob)
filepaths = sorted(
    frozenset(
        itertools.chain.from_iterable(
            glob.iglob(glob_path, recursive=True) for glob_path in glob_paths
        )
    )
)

for filepath in filepaths:

    if args.verbose:
        print(filepath)

    bump(filepath)