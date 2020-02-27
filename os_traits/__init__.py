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

import importlib
import pkgutil
import re
import sys

import pbr.version

THIS_NAME = __name__
THIS_LIB = sys.modules[THIS_NAME]
TEST_DIR = "%s.tests" % THIS_NAME

__version__ = pbr.version.VersionInfo(THIS_NAME).version_string()

# Any user-specified feature/trait is prefixed with the custom namespace
CUSTOM_NAMESPACE = 'CUSTOM_'


def _symbolize(mod_name, props):
    """Given a reference to a Python module object and an iterable of short
    string names for traits, registers symbols in the module corresponding to
    the full namespaced name for each trait.
    """
    for prop in props:
        leaf_mod = sys.modules[mod_name]
        value_base = '_'.join([m.upper() for m in mod_name.split('.')[1:]])
        value = value_base + '_' + prop.upper()
        setattr(THIS_LIB, value, value)  # os_traits.HW_CPU_X86_SSE
        setattr(leaf_mod, prop, value)  # os_traits.hw.cpu.x86.SSE


def _visualize(mod_name, props, seen=None):
    if mod_name in seen:
        return
    seen.add(mod_name)
    components = mod_name.split('.')
    tab = '   '
    # Print the module name
    indent = tab * (len(components) - 1)
    print('%s%s:' % (indent, components[-1].upper()))
    # Print the properties
    indent = tab * len(components)
    if props:
        print('%s%s' % (indent, ', '.join(props)))


def _walk_submodules(package, recursive, callback, **kwargs):
    """Recursively walk the repository's submodules and invoke a callback for
    each module with the list of short trait names found therein.

    :param package: The package (name or module obj) to start from.
    :param recursive: If True, recurse depth-first.
    :param callback: Callable to be invoked for each module. The signature is::

            callback(mod_name, props, **kwargs)

        * mod_name: the string name of the module (e.g. 'os_traits.hw.cpu').
        * props: an iterable of short string names for traits, gleaned from the
          TRAITS member of that module, defaulting to [].
        * kwargs: The same kwargs as passed to _walk_submodules, useful for
          tracking data across calls.
    :param kwargs: Arbitrary keyword arguments to be passed to the callback on
        each invocation.
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    for loader, mod_name, is_pkg in pkgutil.walk_packages(
            package.__path__, package.__name__ + '.'):
        if TEST_DIR in mod_name:
            continue
        imported = importlib.import_module(mod_name)
        props = getattr(imported, "TRAITS", [])
        callback(mod_name, props, **kwargs)
        if recursive and is_pkg:
            _walk_submodules(mod_name, recursive, callback, **kwargs)


# This is where the names defined in submodules are imported by recursively
# importing all submodules/subpackages and symbolizing their TRAITS
_walk_submodules(sys.modules.get(__name__), True, _symbolize)


def get_traits(prefix=None, suffix=None):
    """Returns the trait strings in the os_traits module, optionally filtered
    by a supplied prefix and suffix.

    :param prefix: Optional string prefix to filter by. e.g. 'HW_'
    :param suffix: Optional string suffix to filter by, e.g. 'SSE'
    """
    prefix = prefix or ""
    suffix = suffix or ""
    return [
        v for k, v in sys.modules[__name__].__dict__.items()
        if isinstance(v, str) and
        not k.startswith('_') and
        v.startswith(prefix) and
        v.endswith(suffix) and
        # skip module constants
        k not in ('CUSTOM_NAMESPACE', 'THIS_NAME', 'THIS_LIB', 'TEST_DIR')
    ]


def check_traits(traits, prefix=None):
    """Returns a tuple of two trait string sets, the first set contains valid
    traits, and the second contains others.

    :param traits: An iterable contains trait strings.
    :param prefix: Optional string prefix to filter by. e.g. 'HW_'
    """
    trait_set = set(traits)
    valid_trait_set = set(get_traits(prefix))

    valid_traits = trait_set & valid_trait_set

    return (valid_traits, trait_set - valid_traits)


def is_custom(trait):
    """Returns True if the trait string represents a custom trait, or False
    otherwise.

    :param trait: String name of the trait
    """
    return trait.startswith(CUSTOM_NAMESPACE)


def normalize_name(name):
    """Converts an input string to a legal* custom trait name.

    Legal custom trait names are prefixed with CUSTOM_ and contain only the
    characters A-Z, 0-9, and _ (underscore).

    *Does not attempt to handle length restrictions.

    :param name: A string to be converted.
    :return: A legal* custom trait name.
    """
    if name is None:
        return None
    # Replace non-alphanumeric characters with underscores
    norm_name = re.sub('[^0-9A-Za-z]+', '_', name)
    # Bug #1762789: Do .upper after replacing non alphanumerics.
    return CUSTOM_NAMESPACE + norm_name.upper()


def print_tree():
    """Print (to stdout) a visual representation of all the namespaces and the
    (short) trait names defined therein.

    """
    _walk_submodules(sys.modules.get(__name__), True, _visualize, seen=set())
