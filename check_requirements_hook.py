#!/usr/bin/env python
# coding: utf-8

import argparse
import sys
import pkg_resources


def _create_parser():
	parser = argparse.ArgumentParser(description='Check if all requirements are installed.')
	parser.add_argument('--requirements-file',
	 				metavar='r',
	 				type=str,
	 				help='The requirements file to check',
	 				default='requirements.txt')
	return parser


def open_requirements(requirements_file):
	with open(requirements_file) as requirements:
		return requirements.readlines()


def main():
	
	parser = _create_parser()
	args = parser.parse_args()
	dependencies = open_requirements(args.requirements_file)
	try:
		pkg_resources.require(dependencies)
		sys.exit(0)
	except (pkg_resources.DistributionNotFound, pkg_resources.VersionConflict):
		sys.exit(1)


if __name__ == '__main__':
	main()
