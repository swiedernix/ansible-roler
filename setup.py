#!/usr/bin/env python
"""Setup script for the package."""

import re
import os
import io
from setuptools import find_packages
from setuptools import setup

PACKAGE_NAME = "ansibleroler"


def get_property(prop, project):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
                       open(os.path.join(current_dir, project, '__init__.py')).read())
    return result.group(1)


def get_readme(filename='README.md'):
    this = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(this, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name=get_property("__project__", PACKAGE_NAME),
    version=get_property("__version__", PACKAGE_NAME),
    description=("Command line tool to template the structure of a new ansible role."),
    keywords="ansible cli role template",
    author=get_property("__author__", PACKAGE_NAME),
    author_email=get_property("__email__", PACKAGE_NAME),
    license=get_property("__license__", PACKAGE_NAME),
    url="https://github.com/xoxys/ansible-role",
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    package_dir={'ansibleroler': 'ansibleroler'},
    package_data={
        'ansibleroler': [
            'static/config/*.ini',
            'static/config/*.yml',
            'static/templates/*'
        ],
    },
    zip_safe=False,
    install_requires=[
        "six",
        "appdirs",
        "jinja2",
        "PyYAML",
        "configparser"
    ],
    entry_points={
        'console_scripts': [
            'ansible-roler = ansibleroler.__main__:main'
        ]
    }
)
