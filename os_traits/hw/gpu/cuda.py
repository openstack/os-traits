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

"""
CUDA
----

Applications that need to perform massively parallel operations, like
processing large arrays, may use the CUDA framework to accelerate their
processing on graphics processing units (GPUs). The CUDA framework has two
complementary pieces to it.

There are a set of GPU instruction set extensions that are implemented by
various graphics cards. These instruction set extensions are known as the CUDA
Compute Capability.

The second part of the framework is an SDK that allows developers to take
advantage of the hardware's instruction set extensions of a particular version
(a specific CUDA Compute Capability version, that is).

An application will link with a version of the CUDA SDK, and the version of the
CUDA SDK controls which CUDA Compute Capability versions the application will
be able to work with.

The ``os_traits.hw.gpu.cuda`` module contains traits for both the CUDA compute
capability version as well as the CUDA SDK version. For example,
``os_traits.hw.gpu.cuda.COMPUTE_CAPABILITY_V3_2`` and
``os_traits.hw.gpu.cuda.SDK_V6_5``.

The ``os_traits.hw.gpu.cuda`` module contains a utility function called
``compute_capabilities_supported()`` that accepts a trait indicating the CUDA
SDK version and returns a ``set()`` containing the matching CUDA compute
capability traits that that version of the CUDA SDK knows how to utilize.

Here is an example of listing the CUDA compute capability version traits that
the CUDA SDK 8.0 is capable of working with::

    >>> from os_traits.hw.gpu import cuda
    >>> import pprint
    >>>
    >>> sdk8_caps = cuda.compute_capabilities_supported(cuda.SDK_V8_0)
    >>> pprint.pprint(sdk8_caps)
    set(['HW_GPU_CUDA_COMPUTE_CAPABILITY_V2_0',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V2_1',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_0',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_2',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_5',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_7',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V5_0',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V5_2',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V5_3',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V6_0',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V6_1',
         'HW_GPU_CUDA_COMPUTE_CAPABILITY_V6_2'])

For more information on CUDA, see the `Wikipedia article`_.

.. _Wikipedia article: https://en.wikipedia.org/wiki/CUDA
"""


TRAITS = [
    # ref: https://en.wikipedia.org/wiki/CUDA
    # ref: https://developer.nvidia.com/cuda-toolkit-archive
    'COMPUTE_CAPABILITY_V1_0',
    'COMPUTE_CAPABILITY_V1_1',
    'COMPUTE_CAPABILITY_V1_2',
    'COMPUTE_CAPABILITY_V1_3',
    'COMPUTE_CAPABILITY_V2_0',
    'COMPUTE_CAPABILITY_V2_1',
    'COMPUTE_CAPABILITY_V3_0',
    'COMPUTE_CAPABILITY_V3_2',
    'COMPUTE_CAPABILITY_V3_5',
    'COMPUTE_CAPABILITY_V3_7',
    'COMPUTE_CAPABILITY_V5_0',
    'COMPUTE_CAPABILITY_V5_2',
    'COMPUTE_CAPABILITY_V5_3',
    'COMPUTE_CAPABILITY_V6_0',
    'COMPUTE_CAPABILITY_V6_1',
    'COMPUTE_CAPABILITY_V6_2',
    'COMPUTE_CAPABILITY_V7_0',
    'COMPUTE_CAPABILITY_V7_1',
    'COMPUTE_CAPABILITY_V7_2',
    'SDK_V6_5',
    'SDK_V7_5',
    'SDK_V8_0',
    'SDK_V9_0',
    'SDK_V9_1',
    'SDK_V9_2',
    'SDK_V10_0',
]

_CAPS_V1 = [
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V1_0',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V1_1',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V1_2',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V1_3',
]

_CAPS_V2 = [
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V2_0',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V2_1',
]

_CAPS_V3 = [
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_0',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_2',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_5',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V3_7',
]

_CAPS_V5 = [
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V5_0',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V5_2',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V5_3',
]

_CAPS_V6 = [
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V6_0',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V6_1',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V6_2',
]

_CAPS_V7 = [
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V7_0',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V7_1',
    'HW_GPU_CUDA_COMPUTE_CAPABILITY_V7_2',
]

_SDK_COMPUTE_CAP_SUPPORT = {
    'HW_GPU_CUDA_SDK_V6_5': set(
        _CAPS_V1 + _CAPS_V2 + _CAPS_V3 + _CAPS_V5
    ),
    'HW_GPU_CUDA_SDK_V7_5': set(
        _CAPS_V2 + _CAPS_V3 + _CAPS_V5
    ),
    'HW_GPU_CUDA_SDK_V8_0': set(
        _CAPS_V2 + _CAPS_V3 + _CAPS_V5 + _CAPS_V6
    ),
    'HW_GPU_CUDA_SDK_V9_0': set(
        _CAPS_V3 + _CAPS_V5 + _CAPS_V6 + _CAPS_V7
    ),
    'HW_GPU_CUDA_SDK_V9_1': set(
        _CAPS_V3 + _CAPS_V5 + _CAPS_V6 + _CAPS_V7
    ),
    'HW_GPU_CUDA_SDK_V9_2': set(
        _CAPS_V3 + _CAPS_V5 + _CAPS_V6 + _CAPS_V7
    ),
    'HW_GPU_CUDA_SDK_V10_0': set(
        _CAPS_V3 + _CAPS_V5 + _CAPS_V6 + _CAPS_V7
    ),
}


def compute_capabilities_supported(sdk_trait):
    """Given an SDK trait, returns a set of compute capability traits that the
    version of the SDK supports.

    Returns None if no matches were found for the SDK trait.
    """
    return _SDK_COMPUTE_CAP_SUPPORT.get(sdk_trait)
