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

register('SSL')  # SSL crypto
register('IPSEC')  # IP-Sec crypto
register('TLS')  # TLS crypto
register('DIFFIEH')  # Diffie-Hellmann  crypto
register('RSA')  # RSA crypto
register('ECC')  # Eliptic Curve crypto
register('LZS')  # LZS compression
register('DEFLATE')  # Deflate compression
