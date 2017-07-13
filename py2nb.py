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
nbookv3 = nbf.v3.read_py(code)
nbookv4 = nbf.v4.upgrade(nbookv3)
jsonform = nbf.v4.writes(nbookv4)

dest_file = re.sub('\.py$', '.ipynb', source_file)
if os.path.exists(dest_file):
    s = input("Overwrite existing file `{}' (y/[n])? ".format(dest_file))
    if s.casefold() not in {'y', 'yes'}:
        exit()
with open(dest_file, 'w') as f:
    f.write(jsonform)
