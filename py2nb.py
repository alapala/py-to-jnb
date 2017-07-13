#!/usr/bin/env python3

import argparse
import nbformat as nbf
import os
import re
import sys

parser = argparse.ArgumentParser(
    description='Convert Python code file to Jupyter notebook.'
)
parser.add_argument('source', metavar='SOURCE', help='Source file.')
args = parser.parse_args()
source_file = args.source

nb = nbf.v4.new_notebook()
try:
    with open(source_file) as f:
        code = f.read()
except FileNotFoundError:
    print(
        "{}: {}: No such file".format(
            os.path.basename(__file__),
            source_file
        ),
        file=sys.stderr
    )
    exit(1)
nb.cells.append(nbf.v4.new_code_cell(code))

dest_file = re.sub('\.py$', '.ipynb', source_file)
if os.path.exists(dest_file):
    s = input("Overwrite existing file `{}' (y/[n])? ".format(dest_file))
    if s.casefold() not in {'y', 'yes'}:
        exit()
nbf.write(nb, dest_file)
