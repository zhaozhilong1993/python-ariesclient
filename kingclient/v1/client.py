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

from kingclient.common import http
from kingclient.v1 import services
from kingclient.v1 import orders
from kingclient.v1 import prices
from kingclient.v1 import accounts


class Client(object):
    """Client for the King v1 API.

    :param string endpoint: A user-supplied endpoint URL for the king
                            service.
    :param string token: Token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new client for the King v1 API."""
        self.http_client = http._construct_http_client(*args, **kwargs)
        self.services = services.ServiceManager(self.http_client)
        self.orders = orders.OrderManager(self.http_client)
        self.prices = prices.PriceManager(self.http_client)
        self.accounts = accounts.AccountManager(self.http_client)
