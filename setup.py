#!/bin/env python3
'''Setup script.'''
from pathlib import Path
from setuptools import setup, find_packages

THIS_DIRECTORY = Path(__file__).parent

REQUIREMENTS = (THIS_DIRECTORY / "requirements.txt").read_text().split('\n')[:-1]
LONG_DESCRIPTION = (THIS_DIRECTORY / "README.md").read_text()

CONTENT = {
    "name": "citieswithindist",
    "version": "1.0.0",
    "author": "Willow Ciesialka",
    "author_email": "wciesialka@gmail.com",
    "url": "https://github.com/wciesialka/cities-within-distance",
    "description": "Find cities within a certain distance of you.",
    "long_description": LONG_DESCRIPTION,
    "long_description_content_type": "text/markdown",
    "license": "GPL-3.0",
    "packages": find_packages(where="src"),
    "classifiers": [
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    "keywords": "python cities geographical",
    "package_dir": {"": "src"},
    "install_requires": REQUIREMENTS,
    "zip_safe": False,
    "python_requires": ">=3.10.1"
}

setup(**CONTENT)
