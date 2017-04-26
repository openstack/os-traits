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

import os_traits as ot
from os_traits.hw.cpu import x86
from os_traits.hw.nic import offload
from os_traits.tests import base


class TestSymbols(base.TestCase):

    def test_trait(self):
        """Simply tests that the constants from submodules are imported into
        the primary os_traits module space.
        """
        trait = ot.HW_CPU_X86_SSE42
        self.assertEqual("HW_CPU_X86_SSE42", trait)

        # And the "leaf-module" namespace...
        self.assertEqual(x86.SSE42, ot.HW_CPU_X86_SSE42)
        self.assertEqual(offload.TSO, ot.HW_NIC_OFFLOAD_TSO)

    def test_get_symbol_names(self):
        names = ot.get_symbol_names()
        self.assertIn("HW_CPU_X86_AVX2", names)
        self.assertIn("STORAGE_DISK_SSD", names)
        self.assertIn("HW_NIC_SRIOV", names)
        self.assertIn("MISC_SHARES_VIA_AGGREGATE", names)

    def test_get_traits(self):
        traits = ot.get_traits('HW_CPU')
        self.assertIn("HW_CPU_X86_SSE42", traits)
        self.assertIn(ot.HW_CPU_X86_AVX2, traits)
        self.assertNotIn(ot.STORAGE_DISK_SSD, traits)
        self.assertNotIn(ot.HW_NIC_SRIOV, traits)

    def test_check_traits(self):
        traits = set(["HW_CPU_X86_SSE42", "HW_CPU_X86_XOP"])
        not_traits = set(["not_trait1", "not_trait2"])

        check_traits = []
        check_traits.extend(traits)
        check_traits.extend(not_traits)
        self.assertEqual((traits, not_traits),
                         ot.check_traits(check_traits))

    def test_is_custom(self):
        self.assertTrue(ot.is_custom('CUSTOM_FOO'))
        self.assertFalse(ot.is_custom('HW_CPU_X86_SSE42'))
