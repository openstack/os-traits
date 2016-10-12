# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys

import pbr.version
import six

__version__ = pbr.version.VersionInfo(
    'os_traits').version_string()

# Conveniently import all the constants into the main module "namespace"
from os_traits.const import *


def get_symbol_names(prefix=None):
    """
    Returns the names of symbols of trait strings in the os_traits module,
    optionally filtered by a supplied prefix.

    :param prefix: Optional string prefix to filter by. e.g. 'hw:'
    """
    excluded_keys = ('NAMESPACES',)
    excluded_values = NAMESPACES.values()

    return [
        k for k, v in sys.modules[__name__].__dict__.items()
        if isinstance(v, six.string_types) and
        not k.startswith('_') and
        k not in excluded_keys and
        v not in excluded_values and
        (prefix is None or v.startswith(prefix))
    ]


def get_traits(prefix=None):
    """
    Returns the trait strings in the os_traits module, optionally
    filtered by a supplied prefix.

    :param prefix: Optional string prefix to filter by. e.g. 'hw:'
    """
    excluded_keys = ('NAMESPACES',)
    excluded_values = NAMESPACES.values()

    return [
        v for k, v in sys.modules[__name__].__dict__.items()
        if isinstance(v, six.string_types) and
        not k.startswith('_') and
        k not in excluded_keys and
        v not in excluded_values and
        (prefix is None or v.startswith(prefix))
    ]


def check_traits(traits):
    """
    Returns a tuple of two trait string sets, the first set contains valid
    traits, and the second contains others.

    :param traits: An iterable contains trait strings.
    """
    trait_set = set(traits)
    valid_trait_set = set(get_traits())

    valid_traits = trait_set & valid_trait_set

    return (valid_traits, trait_set - valid_traits)
