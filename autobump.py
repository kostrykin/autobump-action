import argparse
import glob
import itertools
import os
import shlex
from datetime import datetime


def bump(filepath: str):
    year = datetime.now().year
    with open(filepath) as file:
        content = file.read()
        content = content.replace(str(year - 1), str(year))
    with open(filepath, 'w') as file:
        file.write(content)


parser = argparse.ArgumentParser()
parser.add_argument('--glob', type=str, required=True)
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--summary', type=str, default='')
args = parser.parse_args()

glob_paths = shlex.split(args.glob)
paths = sorted(
    frozenset(
        itertools.chain.from_iterable(
            glob.iglob(glob_path, recursive=True) for glob_path in glob_paths
        )
    )
)

num_bumps = 0
for filepath in paths:
    if not os.path.isfile(filepath):
        continue

    if args.verbose:
        print(filepath)

    bump(filepath)
    num_bumps += 1

if args.summary:
    with open(args.summary, 'w') as file:
        file.write(f'changed-files-count={num_bumps}')