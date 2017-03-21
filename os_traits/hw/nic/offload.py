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

register('TSO')  # TCP segmentation
register('GRO')  # Generic receive
register('GSO')  # Generic segmentation
register('UFO')  # UDP Fragmentation
register('LRO')  # Large receive
register('LSO')  # Large send
register('TCS')  # TCP Checksum
register('UCS')  # UDP Checksum
register('SCS')  # SCTP Checksum
register('L2CRC')  # Layer-2 CRC
register('FDF')  # Intel Flow-Director Filter
register('RXVLAN')  # VLAN receive tunnel segmentation
register('TXVLAN')  # VLAN transmit tunnel segmentation
register('VXLAN')  # VxLAN tunneling
register('GRE')  # GRE tunneling
register('GENEVE')  # Geneve tunneling
register('TXUDP')  # UDP transmit tunnel segmentation
register('QINQ')  # QinQ specification
register('RDMA')  # remote direct memory access
register('RXHASH')  # receive hashing
