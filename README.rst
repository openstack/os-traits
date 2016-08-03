===============
os-capabilities
===============

A library containing standardized capability strings.

Capabilities are strings that represent a feature of some resource provider.
This library contains the catalog of constants that have been standardized in
the OpenStack community to refer to a particular hardware, virtualization,
storage, network, or device capability.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/os-capabilities
* Source: http://git.openstack.org/cgit/openstack/os-capabilities
* Bugs: http://bugs.launchpad.net/os-capabilities

Usage
------

`os-capabilities` is primarily composed of a set of constants that may be
referenced by simply importing the os_capabilities module and referencing one
of the module's capabilities constants::

    $ python
    Python 2.7.11+ (default, Apr 17 2016, 14:00:29) 
    [GCC 5.3.1 20160413] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import os_capabilities as os_caps
    >>> print os_caps.HW_CPU_X86_SSE42
    hw:cpu:x86:sse42

Don't know what the symbol names are for the `os_capabilities` module? There's
a helper method for that::

    >>> import pprint
    >>> pprint.pprint(os_caps.get_symbol_names())
    [...
    <snip>
    'HW_CPU_X86_AVX2',
    'HW_CPU_X86_SGX',
    'HW_CPU_X86_AVX',
    'HW_CPU_X86_AVX512BW',
    'HW_CPU_X86_AVX512DQ',
    'HW_CPU_X86_SSE',
    'HW_CPU_X86_SHA',
    'HW_CPU_X86_AVX512F',
    'HW_CPU_X86_F16C',
    'HW_CPU_X86_SSE41',
    'HW_CPU_X86_SSE42',
    'HW_CPU_X86_VMX',
    'HW_CPU_X86_ASF',
    'HW_CPU_X86_BMI2',
    'HW_CPU_X86_CLMUL',
    'HW_CPU_X86_AVX512VL',
    'HW_CPU_X86_AVX512PF',
    'HW_CPU_X86_XOP',
    'HW_CPU_X86_BMI',
    'HW_CPU_X86_ABM',
    'HW_CPU_X86_3DNOW']

Want to see the capability strings for a subset of capabilities? There's a method for that too::

    >>> pprint.pprint(os_caps.get_capabilities(os_caps.NAMESPACES['x86']))
    ['hw:cpu:x86:aes-ni',
    'hw:cpu:x86:avx512er',
    'hw:cpu:x86:avx512cd',
    'hw:cpu:x86:tbm',
    'hw:cpu:x86:tsx',
    'hw:cpu:x86:fma3',
    'hw:cpu:x86:svm',
    'hw:cpu:x86:fma4',
    'hw:cpu:x86:mpx',
    'hw:cpu:x86:sse2',
    'hw:cpu:x86:sse3',
    'hw:cpu:x86:mmx',
    'hw:cpu:x86:ssse3',
    'hw:cpu:x86:sse4a',
    'hw:cpu:x86:avx2',
    'hw:cpu:x86:sgx',
    'hw:cpu:x86:avx',
    'hw:cpu:x86:avx512bw',
    'hw:cpu:x86:avx512dq',
    'hw:cpu:x86:sse',
    'hw:cpu:x86:sha',
    'hw:cpu:x86:avx512f',
    'hw:cpu:x86:f16c',
    'hw:cpu:x86:sse41',
    'hw:cpu:x86:sse42',
    'hw:cpu:x86:vmx',
    'hw:cpu:x86:asf',
    'hw:cpu:x86:bmi2',
    'hw:cpu:x86:clmul',
    'hw:cpu:x86:avx512vl',
    'hw:cpu:x86:avx512pf',
    'hw:cpu:x86:xop',
    'hw:cpu:x86:bmi',
    'hw:cpu:x86:abm',
    'hw:cpu:x86:3dnow']
