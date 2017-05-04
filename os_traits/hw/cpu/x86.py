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


TRAITS = [
    # ref: https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions
    'AVX',
    'AVX2',
    'CLMUL',
    'FMA3',
    'FMA4',
    'F16C',
    'MMX',
    'SSE',
    'SSE2',
    'SSE3',
    'SSSE3',
    'SSE41',
    'SSE42',
    'SSE4A',
    'XOP',
    '3DNOW',

    # ref: https://en.wikipedia.org/wiki/AVX-512
    'AVX512F',  # foundation
    'AVX512CD',  # conflict detection
    'AVX512PF',  # prefetch
    'AVX512ER',  # exponential + reciprocal
    'AVX512VL',  # vector length extensions
    'AVX512BW',  # byte + word
    'AVX512DQ',  # double word + quad word
    # ref: https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets
    'ABM',
    'BMI',
    'BMI2',
    'TBM',
    # ref: https://en.wikipedia.org/wiki/AES_instruction_set
    'AESNI',
    # ref: https://en.wikipedia.org/wiki/Intel_SHA_extensions
    'SHA',
    # ref: https://en.wikipedia.org/wiki/Intel_MPX
    'MPX',
    # ref: https://en.wikipedia.org/wiki/Software_Guard_Extensions
    'SGX',
    # ref:
    #    https://en.wikipedia.org/wiki/Transactional_Synchronization_Extensions
    'TSX',
    # ref: https://en.wikipedia.org/wiki/Advanced_Synchronization_Facility
    'ASF',
    # ref: https://en.wikipedia.org/wiki/VT-x
    'VMX',
    # ref: https://en.wikipedia.org/wiki/AMD-V
    'SVM',
]
