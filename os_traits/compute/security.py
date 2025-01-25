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
    # ref: https://specs.openstack.org/openstack/nova-specs/specs/victoria/implemented/add-emulated-virtual-tpm.html  # noqa
    # support for TPM 1.2
    'TPM_1_2',
    # support for TPM 2.0
    'TPM_2_0',
    # support for TPM with TPM interface Specification(TIS)
    'TPM_TIS',
    # support for TPM with Command-Response Buffer(CRB)
    'TPM_CRB',
    # support for the `user` vTPM secret policy
    'TPM_SECRET_SECURITY_USER',
    # support for the `host` vTPM secret policy
    'TPM_SECRET_SECURITY_HOST',
    # support for the `deployment` vTPM secret policy
    'TPM_SECRET_SECURITY_DEPLOYMENT',
    # support for UEFI Secure Boot
    # ref: https://specs.openstack.org/openstack/nova-specs/specs/wallaby/implemented/allow-secure-boot-for-qemu-kvm-guests.html  # noqa
    'UEFI_SECURE_BOOT',
    # support for stateless firmware
    'STATELESS_FIRMWARE'
]
