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

from os_traits import utils

register = utils.register_fn(__name__)

# ref: https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions
register('AVX')
register('AVX2')
register('CLMUL')
register('FMA3')
register('FMA4')
register('F16C')
register('MMX')
register('SSE')
register('SSE2')
register('SSE3')
register('SSSE3')
register('SSE41')
register('SSE42')
register('SSE4A')
register('XOP')
register('3DNOW')
# ref: https://en.wikipedia.org/wiki/AVX-512
register('AVX512F')  # foundation
register('AVX512CD')  # conflict detection
register('AVX512PF')  # prefetch
register('AVX512ER')  # exponential + reciprocal
register('AVX512VL')  # vector length extensions
register('AVX512BW')  # byte + word
register('AVX512DQ')  # double word + quad word
# ref: https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets
register('ABM')
register('BMI')
register('BMI2')
register('TBM')
# ref: https://en.wikipedia.org/wiki/AES_instruction_set
register('AES-NI')
# ref: https://en.wikipedia.org/wiki/Intel_SHA_extensions
register('SHA')
# ref: https://en.wikipedia.org/wiki/Intel_MPX
register('MPX')
# ref: https://en.wikipedia.org/wiki/Software_Guard_Extensions
register('SGX')
# ref: https://en.wikipedia.org/wiki/Transactional_Synchronization_Extensions
register('TSX')
# ref: https://en.wikipedia.org/wiki/Advanced_Synchronization_Facility
register('ASF')
# ref: https://en.wikipedia.org/wiki/VT-x
register('VMX')
# ref: https://en.wikipedia.org/wiki/AMD-V
register('SVM')
