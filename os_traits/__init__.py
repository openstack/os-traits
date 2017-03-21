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

# Any user-specified feature/trait is prefixed with the custom namespace
CUSTOM_NAMESPACE = 'CUSTOM_'

# Each submodule registers its symbols with the os_traits module namespace
from os_traits.hw.cpu import x86  # noqa
from os_traits.hw import nic  # noqa
from os_traits.hw.nic import accel  # noqa
from os_traits.hw.nic import dcb  # noqa
from os_traits.hw.nic import offload  # noqa
from os_traits.hw.nic import sriov  # noqa
from os_traits.storage import disk  # noqa


def get_symbol_names(prefix=None):
    """Returns the names of symbols of trait strings in the os_traits module,
    optionally filtered by a supplied prefix.

    :param prefix: Optional string prefix to filter by. e.g. 'HW_'
    """
    return [
        k for k, v in sys.modules[__name__].__dict__.items()
        if isinstance(v, six.string_types) and
        not k.startswith('_') and
        (prefix is None or v.startswith(prefix))
    ]


def get_traits(prefix=None):
    """Returns the trait strings in the os_traits module, optionally filtered
    by a supplied prefix.

    :param prefix: Optional string prefix to filter by. e.g. 'HW_'
    """
    return [
        v for k, v in sys.modules[__name__].__dict__.items()
        if isinstance(v, six.string_types) and
        not k.startswith('_') and
        (prefix is None or v.startswith(prefix))
    ]


def check_traits(traits):
    """Returns a tuple of two trait string sets, the first set contains valid
    traits, and the second contains others.

    :param traits: An iterable contains trait strings.
    """
    trait_set = set(traits)
    valid_trait_set = set(get_traits())

    valid_traits = trait_set & valid_trait_set

    return (valid_traits, trait_set - valid_traits)


def is_custom(trait):
    """Returns True if the trait string represents a custom trait, or False
    otherwise.

    :param trait: String name of the trait
    """
    return trait.startswith(CUSTOM_NAMESPACE)
