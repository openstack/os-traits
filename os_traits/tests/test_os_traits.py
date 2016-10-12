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
test_os_traits
----------------------------------

Tests for `os_traits` module.
"""

import os_traits as ot
from os_traits.tests import base


class TestOs_traits(base.TestCase):

    def test_trait(self):
        trait = ot.HW_CPU_X86_SSE42
        self.assertEqual("hw:cpu:x86:sse42", trait)

    def test_get_symbol_names(self):
        names = ot.get_symbol_names()
        self.assertIn("HW_CPU_X86_AVX2", names)
        self.assertEqual(35, len(names))

    def test_namespaces(self):
        namespaces = ot.NAMESPACES
        self.assertIn(("hardware", "hw:"), namespaces.items())
        self.assertEqual(4, len(namespaces))

    def test_get_traits(self):
        traits = ot.get_traits(ot.NAMESPACES['x86'])
        self.assertIn("hw:cpu:x86:sse42", traits)
        self.assertEqual(35, len(traits))

    def test_check_traits(self):
        traits = set(["hw:cpu:x86:sse42", "hw:cpu:x86:xop"])
        not_traits = set(["not_trait1", "not_trait2"])

        check_traits = []
        check_traits.extend(traits)
        check_traits.extend(not_traits)
        self.assertEqual((traits, not_traits),
                         ot.check_traits(check_traits))
