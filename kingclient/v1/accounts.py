# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from kingclient.openstack.common.apiclient import base


class Account(base.Resource):
    def __repr__(self):
        return "<Account %s>" % self._info


class AccountManager(base.BaseManager):
    resource_class = Account

    def list(self):
        """Get a list of Account.

        :rtype: list of :class:`Account`
        """
        url = '/account'
        return self._list(url)

    def create(self, value):
        """Create Account.

        :rtype: class:`Account`
        """
        url = '/account'
        return self._post(url, value)
