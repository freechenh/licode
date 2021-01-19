#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: consumer_demo.py
# @Author: dell
# @Date: 2021/1/18  10:38
# @Desc: 
# @Project: licode
# @Source: PyCharm


import atexit
import unittest
# import pytest
import requests
from pact import Consumer, Provider

pact = Consumer('Consumer').has_pact_with(Provider("Provider"))
pact.start_service()
atexit.register(pact.stop_service)


def user(user_name):
    """Fetch a user object by user_name from the server."""
    uri = 'http://localhost:1234/users/' + user_name
    return requests.get(uri).json()


class GetUserInfoContract(unittest.TestCase):
    def test_get_user(self):
        expected = {
            'username': 'UserA',
            'id': 123,
            'groups': ['Editors']
        }

        (pact
         .given('UserA exists and is not an administrator')
         .upon_receiving('a request for UserA')
         .with_request('get', '/users/UserA')
         .will_respond_with(200, body=expected))

        with pact:
            result = user('UserA')

        self.assertEqual(result, expected)

    def test_get_user_userB(self):
        expected = {
            'username': 'UserB',
            'id': 124,
            'groups': ['Editors']
        }

        (pact
         .given('UserB exists and is not an administrator')
         .upon_receiving('a request for UserB')
         .with_request('get', '/users/UserB')
         .will_respond_with(200, body=expected))

        with pact:
            result = user('UserB')

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
