#
# Copyright 2009 Google Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "sstuart@google.com (Stephen Stuart)"

"""
BMP (BGP Monitoring Protocol)

Various constants associated with the protocol, minor version tracks
draft revision number.
"""
__version__ = '0.1'

HEADER_LEN = 44

# version
#
VERSION = 1

# message types
#
MSG_TYPE_ROUTE_MONITORING = 0
MSG_TYPE_STATISTICS_REPORT = 1
MSG_TYPE_PEER_DOWN_NOTIFICATION = 2
MSG_TYPE_STR = {MSG_TYPE_ROUTE_MONITORING: 'Route Monitoring', 
                MSG_TYPE_STATISTICS_REPORT: 'Statistics Report', 
                MSG_TYPE_PEER_DOWN_NOTIFICATION: 'Peer Down Notification'}

# peer types
#
PEER_TYPE_GLOBAL = 0
PEER_TYPE_L3_VPN = 1
PEER_TYPE_STR = {PEER_TYPE_GLOBAL: 'Global', 
                 PEER_TYPE_L3_VPN: 'L3 VPN'}

# peer flags
#
PEER_FLAG_IPV6 = 0x80

# statistics report TLV type codes
#
SR_TYPE_STR = {0: 'prefixes rejected by inbound policy',
               1: '(known) duplicate prefix advertisements',
               2: '(known) duplicate withdraws',
               3: 'updates invalidated due to CLUSTER_LIST loop',
               4: 'updates invalidated due to AS_PATH loop'}
