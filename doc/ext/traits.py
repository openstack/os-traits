# Copyright 2020, Red Hat, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Generate a listing of all known traits."""

import os

import os_traits

REFERENCE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir, 'source',
    'reference',
)


def _generate_trait_list():
    yield 'Available Traits'
    yield '================'
    yield ''
    yield 'Below is a list of all traits currently available.'
    yield ''

    for trait in os_traits.get_traits():
        yield f'- ``{trait}``'

    yield ''


def generate_trait_list(app):
    """Generate a listing of all known traits."""
    with open(os.path.join(REFERENCE_DIR, 'traits.rst'), 'w+') as fh:
        for line in _generate_trait_list():
            print(line, file=fh)


def setup(app):
    app.connect('builder-inited', generate_trait_list)
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
