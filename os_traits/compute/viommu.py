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

    # traits corresponding to the allowed values of "hw_iommu_model"
    # image metadata property
    # Please check VIOMMUModel under /nova/objects/fields.py
    # we do not include None as by default no iommu will be provided
    'MODEL_INTEL',
    'MODEL_SMMUV3',
    'MODEL_VIRTIO',
    'MODEL_AUTO',
]
