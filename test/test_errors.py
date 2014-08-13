# Copyright 2009-2014 MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test the errors module."""

import sys

sys.path[0:0] = [""]

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from test import unittest
from test.utils import connected


class TestErrors(unittest.TestCase):

    def test_base_exception(self):
        # connected(MongoClient(...)) with a bad port raises AutoReconnect.
        self.assertRaises(PyMongoError,
                          connected, MongoClient(port=0, serverWaitTimeMS=100))


if __name__ == '__main__':
    unittest.main()
