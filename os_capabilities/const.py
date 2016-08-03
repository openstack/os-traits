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

# All hardware-specific features are prefixed with this namespace
_HW_NS = 'hw:'

# All CPU-specific features are prefixed with this namespace
_CPU_NS = _HW_NS + 'cpu:'

_CPU_X86_NS = _CPU_NS + 'x86:'

# ref: https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions
HW_CPU_X86_AVX = _CPU_X86_NS + 'avx'
HW_CPU_X86_AVX2 = _CPU_X86_NS + 'avx2'
HW_CPU_X86_CLMUL = _CPU_X86_NS + 'clmul'
HW_CPU_X86_FMA3 = _CPU_X86_NS + 'fma3'
HW_CPU_X86_FMA4 = _CPU_X86_NS + 'fma4'
HW_CPU_X86_F16C = _CPU_X86_NS + 'f16c'
HW_CPU_X86_MMX = _CPU_X86_NS + 'mmx'
HW_CPU_X86_SSE = _CPU_X86_NS + 'sse'
HW_CPU_X86_SSE2 = _CPU_X86_NS + 'sse2'
HW_CPU_X86_SSE3 = _CPU_X86_NS + 'sse3'
HW_CPU_X86_SSSE3 = _CPU_X86_NS + 'ssse3'
HW_CPU_X86_SSE41 = _CPU_X86_NS + 'sse41'
HW_CPU_X86_SSE42 = _CPU_X86_NS + 'sse42'
HW_CPU_X86_SSE4A = _CPU_X86_NS + 'sse4a'
HW_CPU_X86_XOP = _CPU_X86_NS + 'xop'
HW_CPU_X86_3DNOW = _CPU_X86_NS + '3dnow'
# ref: https://en.wikipedia.org/wiki/AVX-512
HW_CPU_X86_AVX512F = _CPU_X86_NS + 'avx512f'  # foundation
HW_CPU_X86_AVX512CD = _CPU_X86_NS + 'avx512cd'  # conflict detection
HW_CPU_X86_AVX512PF = _CPU_X86_NS + 'avx512pf'  # prefetch
HW_CPU_X86_AVX512ER = _CPU_X86_NS + 'avx512er'  # exponential + reciprocal
HW_CPU_X86_AVX512VL = _CPU_X86_NS + 'avx512vl'  # vector length extensions
HW_CPU_X86_AVX512BW = _CPU_X86_NS + 'avx512bw'  # byte + word
HW_CPU_X86_AVX512DQ = _CPU_X86_NS + 'avx512dq'  # double word + quad word
# ref: https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets
HW_CPU_X86_ABM = _CPU_X86_NS + 'abm'
HW_CPU_X86_BMI = _CPU_X86_NS + 'bmi'
HW_CPU_X86_BMI2 = _CPU_X86_NS + 'bmi2'
HW_CPU_X86_TBM = _CPU_X86_NS + 'tbm'
# ref: https://en.wikipedia.org/wiki/AES_instruction_set
HW_CPU_X86_AESNI = _CPU_X86_NS + 'aes-ni'
# ref: https://en.wikipedia.org/wiki/Intel_SHA_extensions
HW_CPU_X86_SHA = _CPU_X86_NS + 'sha'
# ref: https://en.wikipedia.org/wiki/Intel_MPX
HW_CPU_X86_MPX = _CPU_X86_NS + 'mpx'
# ref: https://en.wikipedia.org/wiki/Software_Guard_Extensions
HW_CPU_X86_SGX = _CPU_X86_NS + 'sgx'
# ref: https://en.wikipedia.org/wiki/Transactional_Synchronization_Extensions
HW_CPU_X86_TSX = _CPU_X86_NS + 'tsx'
# ref: https://en.wikipedia.org/wiki/Advanced_Synchronization_Facility
HW_CPU_X86_ASF = _CPU_X86_NS + 'asf'
# ref: https://en.wikipedia.org/wiki/VT-x
HW_CPU_X86_VMX = _CPU_X86_NS + 'vmx'
# ref: https://en.wikipedia.org/wiki/AMD-V
HW_CPU_X86_SVM = _CPU_X86_NS + 'svm'

NAMESPACES = {
    'hardware': _HW_NS,
    'hw': _HW_NS,
    'cpu': _CPU_NS,
    'x86': _CPU_X86_NS,
}
