import os
import re
import sys
import setuptools

here = os.path.dirname(__file__)

# Read version number
pat = r'__version__ = \((\w+), (\w+), (\w+)\)'
with open(os.path.join(here, 'jinjatag', 'version.py')) as f:
    version = '.'.join(re.search(pat, f.read()).groups())

requirements = [
    "jinja2>=2.5",
    "six",
    ]

# Require the external importlib package if python 2.6
version_tuple = sys.version_info
if version_tuple[0] < 3 and version_tuple[1] < 7:
    requirements.append('importlib')

setuptools.setup(
    name = "jinjatag",
    version = version,
    author = "Dave Mankoff",
    author_email = "mankyd@gmail.com",
    description = "A library to make Jinja2 Extensions Easy",
    long_description = open(os.path.join(here, "README.md")).read(),
    test_suite = 'jinjatag.tests.test_all',
    license = "GPLv3",
    url = "https://github.com/mankyd/jinjatag",
    install_requires=requirements,
    packages = [
        "jinjatag",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 3.5",
    ]
)
