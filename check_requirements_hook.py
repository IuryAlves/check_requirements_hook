#!/usr/bin/env python
# coding: utf-8

import argparse
import sys
import pkg_resources


def _create_parser():
    parser = argparse.ArgumentParser(
        description='Check if all requirements are installed.')
    parser.add_argument('--requirements-file',
                        metavar='r',
                        type=str,
                        help='The requirements file to check',
                        default='requirements.txt')
    return parser


def open_requirements(requirements_file):
    with open(requirements_file) as requirements:
        return requirements.readlines()


def print_green(message):
    template = '\033[92m{message}\033[0m'
    print(template.format(message=message))


def print_red(message):
    template = '\033[91m{message}\033[0m'
    print(template.format(message=message))


def main():

    parser = _create_parser()
    args = parser.parse_args()
    dependencies = open_requirements(args.requirements_file)
    try:
        pkg_resources.require(dependencies)
        print_green('Your requirements are up to date!')
        sys.exit(0)
    except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
        print_red('You must update your requirements!')
        sys.exit(1)


if __name__ == '__main__':
    main()
