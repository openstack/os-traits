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
_HW_NS = 'HW_'

# All CPU-specific features are prefixed with this namespace
_CPU_NS = _HW_NS + 'CPU_'

_CPU_X86_NS = _CPU_NS + 'X86_'

# ref: https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions
HW_CPU_X86_AVX = _CPU_X86_NS + 'AVX'
HW_CPU_X86_AVX2 = _CPU_X86_NS + 'AVX2'
HW_CPU_X86_CLMUL = _CPU_X86_NS + 'CLMUL'
HW_CPU_X86_FMA3 = _CPU_X86_NS + 'FMA3'
HW_CPU_X86_FMA4 = _CPU_X86_NS + 'FMA4'
HW_CPU_X86_F16C = _CPU_X86_NS + 'F16C'
HW_CPU_X86_MMX = _CPU_X86_NS + 'MMX'
HW_CPU_X86_SSE = _CPU_X86_NS + 'SSE'
HW_CPU_X86_SSE2 = _CPU_X86_NS + 'SSE2'
HW_CPU_X86_SSE3 = _CPU_X86_NS + 'SSE3'
HW_CPU_X86_SSSE3 = _CPU_X86_NS + 'SSSE3'
HW_CPU_X86_SSE41 = _CPU_X86_NS + 'SSE41'
HW_CPU_X86_SSE42 = _CPU_X86_NS + 'SSE42'
HW_CPU_X86_SSE4A = _CPU_X86_NS + 'SSE4A'
HW_CPU_X86_XOP = _CPU_X86_NS + 'XOP'
HW_CPU_X86_3DNOW = _CPU_X86_NS + '3DNOW'
# ref: https://en.wikipedia.org/wiki/AVX-512
HW_CPU_X86_AVX512F = _CPU_X86_NS + 'AVX512F'  # foundation
HW_CPU_X86_AVX512CD = _CPU_X86_NS + 'AVX512CD'  # conflict detection
HW_CPU_X86_AVX512PF = _CPU_X86_NS + 'AVX512PF'  # prefetch
HW_CPU_X86_AVX512ER = _CPU_X86_NS + 'AVX512ER'  # exponential + reciprocal
HW_CPU_X86_AVX512VL = _CPU_X86_NS + 'AVX512VL'  # vector length extensions
HW_CPU_X86_AVX512BW = _CPU_X86_NS + 'AVX512BW'  # byte + word
HW_CPU_X86_AVX512DQ = _CPU_X86_NS + 'AVX512DQ'  # double word + quad word
# ref: https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets
HW_CPU_X86_ABM = _CPU_X86_NS + 'ABM'
HW_CPU_X86_BMI = _CPU_X86_NS + 'BMI'
HW_CPU_X86_BMI2 = _CPU_X86_NS + 'BMI2'
HW_CPU_X86_TBM = _CPU_X86_NS + 'TBM'
# ref: https://en.wikipedia.org/wiki/AES_instruction_set
HW_CPU_X86_AESNI = _CPU_X86_NS + 'AES-NI'
# ref: https://en.wikipedia.org/wiki/Intel_SHA_extensions
HW_CPU_X86_SHA = _CPU_X86_NS + 'SHA'
# ref: https://en.wikipedia.org/wiki/Intel_MPX
HW_CPU_X86_MPX = _CPU_X86_NS + 'MPX'
# ref: https://en.wikipedia.org/wiki/Software_Guard_Extensions
HW_CPU_X86_SGX = _CPU_X86_NS + 'SGX'
# ref: https://en.wikipedia.org/wiki/Transactional_Synchronization_Extensions
HW_CPU_X86_TSX = _CPU_X86_NS + 'TSX'
# ref: https://en.wikipedia.org/wiki/Advanced_Synchronization_Facility
HW_CPU_X86_ASF = _CPU_X86_NS + 'ASF'
# ref: https://en.wikipedia.org/wiki/VT-x
HW_CPU_X86_VMX = _CPU_X86_NS + 'VMX'
# ref: https://en.wikipedia.org/wiki/AMD-V
HW_CPU_X86_SVM = _CPU_X86_NS + 'SVM'

NAMESPACES = {
    'HARDWARE': _HW_NS,
    'HW': _HW_NS,
    'CPU': _CPU_NS,
    'X86': _CPU_X86_NS,
}
