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
    # Traits corresponding to the allowed values of "hw_sound_model"
    # image metadata property. These are used by the nova libvirt driver and
    # are listed at https://libvirt.org/formatdomain.html#sound-devices
    'MODEL_SB16',
    'MODEL_ES1370',
    'MODEL_PCSPK',
    'MODEL_AC97',
    'MODEL_ICH6',
    'MODEL_ICH9',
    'MODEL_USB',
    'MODEL_VIRTIO'
]
