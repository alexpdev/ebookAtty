# ebookatty

![License](https://img.shields.io/badge/License-LGPL-blue?style=for-the-badge&logo=appveyor)
![Testing](https://img.shields.io/badge/Testing-Pytest-orange?style=for-the-badge&logo=appveyor)
![Python](https://img.shields.io/badge/Python-3.0%2B-red?style=for-the-badge&logo=appveyor)

-------------------------

Simple utility that extracts embedded metadata in common ebook formats. Works on mobi epub and most amazon kindle filetypes.
Includes a library of classes and functions for dealing with metadata, as well as a CLI to use as a standalone tool.
It is still a work in progress.

## Features

* succesfully extracts metadata from .mobi .kfx .epub .azw .azw3 file formats
* Extremely simple
* requires no external dependencies

## Requirements

* Python 3.3+
* Tested on Windows and Linux

## Installing

```Linux
pip install ebookatty
```

## Instructions

Using as a command line interface is super easy:

```Linux
ebookatty path/to/ebook.epub
```

or import into your project...

```python
from ebookatty import get_metadata, MetadataFetcher
```

## License / EULA

GNU LGPL v3.0
[LICENSE FILE](./LICENSE.md)
