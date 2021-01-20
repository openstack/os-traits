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
    # The virt driver supports associating a tag with a device *at boot time*
    'DEVICE_TAGGING',
    # A provider with this trait is a compute *node*. (As distinct from
    # "compute host" or "hypervisor". These may be synonymous in some cases,
    # but the distinction matters e.g. when using the ironic virt driver.)
    'NODE',
    # The virt driver supports trusted image certificate validation
    'TRUSTED_CERTS',
    # The virt driver supports cold migrating to the same compute service host.
    # This really only works for a cluster-type hypervisor driver like the
    # vCenter driver which is a single compute service host managing a vCenter
    # cluster of potentially hundreds of ESXi hosts. Note that this trait will
    # not make sense to use in GET /allocation_candidates until/unless there is
    # a way to tie it to the condition of SAME_HOST-ness.
    'SAME_HOST_COLD_MIGRATE',
    # The virt driver supports rescuing boot from volume instances.
    'RESCUE_BFV',
    # The compute manager supports handling accelerator requests.
    'ACCELERATORS',
    # The compute manager supports the `socket` value for the
    # hw_pci_numa_affinity_policy image property/flavor extra spec.
    'SOCKET_PCI_NUMA_AFFINITY',
]
