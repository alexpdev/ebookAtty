#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from pybook_metadata.pybook_metadata import get_metadata, MetadataFetcher, cliparse

def main():
    cliparse(sys.argv[1:])

__version__ = "0.1"