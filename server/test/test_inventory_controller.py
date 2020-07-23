# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from server.models.lot_number_body import LotNumberBody  # noqa: E501
from server.models.part_number_body import PartNumberBody  # noqa: E501
from server.test import BaseTestCase


class TestInventoryController(BaseTestCase):
    """InventoryController integration test stubs"""

    def test_add_ln(self):
        """Test case for add_ln

        Add a new lot number to a part number
        """
        body = LotNumberBody()
        response = self.client.open(
            '/inventory/lot_number',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_pn(self):
        """Test case for add_pn

        Add a new work order to the server
        """
        body = PartNumberBody()
        response = self.client.open(
            '/inventory/part_number',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_inv(self):
        """Test case for get_inv

        Get the information of all inventory
        """
        response = self.client.open(
            '/inventory',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_ln(self):
        """Test case for get_ln

        Get the information of a lot number
        """
        query_string = [('lot_number', 'lot_number_example')]
        response = self.client.open(
            '/inventory/lot_number',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pn(self):
        """Test case for get_pn

        Get the information of a part number
        """
        query_string = [('part_number', 'part_number_example')]
        response = self.client.open(
            '/inventory/part_number',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_ln(self):
        """Test case for update_ln

        Update an item
        """
        body = LotNumberBody()
        response = self.client.open(
            '/inventory/lot_number',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pn(self):
        """Test case for update_pn

        Update a part number
        """
        body = PartNumberBody()
        response = self.client.open(
            '/inventory/part_number',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
