#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='aws-check-codepipeline-deployed-stacks',
    version='0.0.1rc1',
    scripts=['aws-check-codepipeline-deployed-stacks'],
    author='P. H.',
    author_email='pip-aws-check-cp-deployed-stacks.perfide@safersignup.de',
    description='Find AWS stacks which are not deployed by CodePipline',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/perfide/aws-check-codepipeline-deployed-stacks',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
    ],
)
