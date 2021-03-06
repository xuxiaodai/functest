#!/usr/bin/env python

# Copyright (c) 2017 Cable Television Laboratories, Inc. and others.
#
# This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0

# pylint: disable=missing-docstring

import unittest

from functest.opnfv_tests.openstack.snaps import snaps_suite_builder
from functest.opnfv_tests.openstack.snaps.snaps_test_runner import \
    SnapsTestRunner


class ConnectionCheck(SnapsTestRunner):
    """
    This test executes the Python Tests included with the SNAPS libraries
    that simply obtain the different OpenStack clients and may perform
    simple queries
    """
    def __init__(self, **kwargs):
        if "case_name" not in kwargs:
            kwargs["case_name"] = "connection_check"
        super(ConnectionCheck, self).__init__(**kwargs)

        self.suite = unittest.TestSuite()

    def run(self, **kwargs):
        """
        Builds the test suite then calls super.run()
        :param kwargs: the arguments to pass on
        :return:
        """
        snaps_suite_builder.add_openstack_client_tests(
            suite=self.suite,
            os_creds=self.os_creds,
            ext_net_name=self.ext_net_name,
            use_keystone=self.use_keystone)
        return super(ConnectionCheck, self).run()
