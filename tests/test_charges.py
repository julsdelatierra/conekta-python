#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from . import BaseEndpointTestCase

from conekta import Conekta


class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_card_charge_done(self):
        response = self.client.Charge.create(self.card_charge_object)
        assert 'id' in response.to_json()

    def test_cash_charge_done(self):
        response = self.client.Charge.create(self.cash_charge_object)
        assert 'id' in response.to_json()

    def test_bank_charge_done(self):
        response = self.client.Charge.create(self.bank_charge_object)
        assert 'id' in response.to_json()

    def test_card_charge_authentication_fail(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.card_charge_object)
        print response.to_json()['error']['type']
        assert 'authentication_error' == response.to_json()['error']['type']

    def test_cash_charge_authentication_fail(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.cash_charge_object)
        assert 'authentication_error' == response.to_json()['error']['type']

    def test_bank_charge_authentication_fail(self):
        self.client.api_key = ''
        response = self.client.Charge.create(self.bank_charge_object)
        assert 'authentication_error' == response.to_json()['error']['type']
