=========
Reference
=========

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
