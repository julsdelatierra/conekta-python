#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from . import BaseEndpointTestCase


class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_card_charge_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.card_charge_object)
        assert charge.id
        charge.refund(10000)
        self.assertEqual(charge['status'], 'partially_refunded')
        charge.refund()
        self.assertEqual(charge['status'], 'refunded')
        retrieved_charge = self.client.Charge.retrieve(charge.id)
        assert charge.id

    def test_cash_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.cash_charge_object)
        assert charge.id

    def test_bank_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.bank_charge_object)
        assert charge.id

    def test_card_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.card_charge_object)

    def test_cash_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.cash_charge_object)

    def test_bank_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.bank_charge_object)

    def test_log_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        logs = self.client.Log.all()
        self.assertIsInstance(logs[0], self.client.Log)
        retrieved_log = self.client.Log.retrieve(logs[0].id)
        assert retrieved_log.id

    def test_event_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        events = self.client.Event.all()
        self.assertIsInstance(events[0], self.client.Event)
        retrieved_event = self.client.Event.retrieve(events[0].id)
        assert retrieved_event.id

