#!/usr/bin/env python3

import os
import re
import csv
import sys
import argparse

from collections import defaultdict


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument("mapping")

    args = parser.parse_args(args)

    for read in list_chimera(args.mapping):
        print(read)


def parse_mapping(filename):
    read2ref = defaultdict(list)

    mapping = csv.reader(open(filename, "r"), delimiter='\t')
    for m in mapping:
        que_name = m[0]

        ref_name = m[5]

        read2ref[que_name].append(ref_name)

    return read2ref


def list_chimera(filename):
    read2ref = parse_mapping(filename)

    for (reads, refs) in read2ref.items():
        if len(set(refs)) > 1:
            yield reads


if __name__ == "__main__":
    main(sys.argv[1:])
