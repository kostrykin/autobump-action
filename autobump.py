import argparse
import glob
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

for filepath in glob.glob(args.glob, recursive=True):

    if args.verbose:
        print(filepath)

    bump(filepath)