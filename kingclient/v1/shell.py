# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging
import os

from kingclient.common import utils

logger = logging.getLogger(__name__)

SERVICES_FIELDS = (
    'hostname',
    'engine_id',
    'host',
    'topic',
    'updated_at',
    'status'
)

ACCOUNT_FIELDS = (
    'id',
    'os_user_id',
    'account_id',
    'account_level',
    'account_money',
    'created_at'
)

def do_service_list(kc, args=None):
    '''List the King engines.'''
    services = kc.services.list()
    utils.print_list(services, SERVICES_FIELDS, sortby_index=1)


@utils.arg('--username',
           type=str,
           help='the username.')
@utils.arg('--password',
           help='the user password.')
@utils.arg('--type',
           help='the cloud type,such as OpenStack,Aliyun,AWS.')
def do_account_create(kc, args=None):
    '''Create the account.'''
    os_project_name = os.getenv('OS_PROJECT_NAME')
    os_username = os.getenv('OS_USERNAME')
    os_auth_url = os.getenv('OS_AUTH_URL')

    if not os_project_name or not os_username \
            or os_auth_url:
        print 'OS_PROJECT_NAME or OS_USERNAME or OS_AUTH_URL not exit in env'
        return False

    value = {"username": args.username,
             "password": args.password,
             "type": args.type,
             "os_username": os_username,
             "os_project": os_project_name,
             "os_auth_url": os_auth_url
             }
    body = {"account": value}
    account = kc.accounts.create(body)
    utils.print_list(account.to_dict(), ACCOUNT_FIELDS, sortby_index=1)


def _extract_metadata(args):
    metadata = {}
    for metadatum in args.metadata:
        # unset doesn't require a val, so we have the if/else
        if '=' in metadatum:
            (key, value) = metadatum.split('=', 1)
        else:
            key = metadatum
            value = None

        metadata[key] = value
    return metadata
