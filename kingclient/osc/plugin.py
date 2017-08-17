#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import logging

from openstackclient.common import utils

LOG = logging.getLogger(__name__)

DEFAULT_CHARGING_API_VERSION = '1'
API_VERSION_OPTION = 'os_charging_api_version'
API_NAME = 'charging'
API_VERSIONS = {
    '1': 'kingclient.v1.client.Client',
}


def make_client(instance):
    """Returns an charging service client"""
    king_client = utils.get_client_class(
        API_NAME,
        instance._api_version[API_NAME],
        API_VERSIONS)
    LOG.debug('Instantiating charging client: %s', king_client)

    kwargs = {'region_name': instance.region_name,
              'interface': instance.interface}

    if instance.session:
        kwargs.update({'session': instance.session,
                       'service_type': API_NAME})
    else:
        endpoint = instance.get_endpoint_for_service_type(
            API_NAME,
            region_name=instance.region_name,
            interface=instance.interface,
        )

        kwargs.update({'endpoint': endpoint,
                       'auth_url': instance.auth.auth_url,
                       'username': instance.auth_ref.username,
                       'token': instance.auth_ref.auth_token})

    client = king_client(**kwargs)

    return client


def build_option_parser(parser):
    """Hook to add global options"""
    parser.add_argument(
        '--os-charging-api-version',
        metavar='<charging-api-version>',
        default=utils.env(
            'OS_CHARGING_API_VERSION',
            default=DEFAULT_CHARGING_API_VERSION),
        help='Charging API version, default=' +
             DEFAULT_CHARGING_API_VERSION +
             ' (Env: OS_CHARGING_API_VERSION)')
    return parser
