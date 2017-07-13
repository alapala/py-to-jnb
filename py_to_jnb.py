#!/usr/bin/env python3

import argparse
import nbformat as nbf
import os
import re
import sys


def notebook_cell_parse(codestream):
    '''Parse a stream of Python code into a Jupyter notebook with cells.'''
    nb = nbf.v4.new_notebook()
    chunk = ''
    for line in codestream:
        if contains_new_cell_delimiter(line) and len(chunk) > 0:
            code_cell = nbf.v4.new_code_cell(chunk.rstrip())
            nb.cells.append(code_cell)
            chunk = ''
        chunk += line
    if len(chunk) > 0:
        code_cell = nbf.v4.new_code_cell(chunk.rstrip())
        nb.cells.append(code_cell)
    return nb


def contains_new_cell_delimiter(s):
    '''Return a regex match object if string contains new cell delimiter.'''
    return re.search('#[\s#]*(.*)-{4,}\s*$', s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert Python code file to Jupyter notebook.'
    )
    parser.add_argument('source', metavar='SOURCE', help='Source file.')
    args = parser.parse_args()
    source_file = args.source

    try:
        with open(source_file) as fp:
            nb = notebook_cell_parse(fp)
    except FileNotFoundError:
        print(
            "{}: {}: No such file".format(
                os.path.basename(__file__),
                source_file
            ),
            file=sys.stderr
        )
        sys.exit(1)

    dest_file = re.sub('(\.py)?$', '.ipynb', source_file)
    if os.path.exists(dest_file):
        s = input("Overwrite existing file `{}' (y/[n])? ".format(dest_file))
        if s.casefold() not in {'y', 'yes'}:
            exit()
    nbf.write(nb, dest_file)
