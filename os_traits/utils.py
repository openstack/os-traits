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

import functools
import sys

import os_traits


def symbolize(mod_name, name):
    """Given a reference to a Python module object and a short string name for
    a trait, registers a symbol in the module that corresponds to the full
    namespaced trait name.

    For example, if called like so:

    :code:

    # In file /os_traits/hw/cpu/x86.py

    import functools

    from os_traits import utils

    mod_register = functools.partial(utils.symbolize, __name__)

    mod_register('AVX2')
    mod_register('SSE')

    Would end up creating the following symbols:

    os_traits.hw.cpu.x86.AVX2 with the value of 'HW_CPU_X86_AVX2'
    os_traits.hw.cpu.x86.SSE with the value of 'HW_CPU_X86_SSE'
    os_traits.HW_CPU_X86_AVX2 with the value of 'HW_CPU_X86_AVX2'
    os_traits.HW_CPU_X86_SSE with the value of 'HW_CPU_X86_SSE'
    """
    leaf_mod = sys.modules[mod_name]
    value_base = '_'.join([m.upper() for m in mod_name.split('.')[1:]])
    value = value_base + '_' + name.upper()
    setattr(os_traits, value, value)  # os_traits.HW_CPU_X86_SSE
    setattr(leaf_mod, name.upper(), value)  # os_traits.hw.cpu.x86.SSE


def register_fn(mod_name):
    return functools.partial(symbolize, mod_name)
