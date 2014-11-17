#!/usr/bin/env python
# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

from setuptools import setup, find_packages


def get_version_string():
    version = None
    sys.path.insert(0, os.path.join(os.getcwd()))
    from st2client import __version__
    version = __version__
    sys.path.pop(0)
    return version


def get_requirements():
    with open('requirements.txt') as f:
        required = f.read().splitlines()
    return required


setup(
    name='st2client',
    version=get_version_string(),
    description='CLI and python client library for the StackStorm (st2) automation platform.',
    author='StackStorm',
    author_email='info@stackstorm.com',
    url='http://www.stackstorm.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points={
        'console_scripts': [
            'st2 = st2client.shell:main'
        ]
    }
)
