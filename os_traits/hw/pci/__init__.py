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

# Characteristics of PCI devices
TRAITS = [
    # PCI device can be live-migrated from one compute node to another
    # with the same device.
    'LIVE_MIGRATABLE',
    # PCI device lifecycle is being managed as "one time use". Compute manager
    # will set reserved=total during assignment and leave it as such during
    # deallocation, requiring an external agent to un-reserve it before it
    # can be used again.
    'ONE_TIME_USE',
]
