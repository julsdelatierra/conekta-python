#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from . import BaseEndpointTestCase


class OrdersEndpointTestCase(BaseEndpointTestCase):

    def test_01_card_charge_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.card_charge_object)
        assert charge.id
        assert charge.status == 'paid'
        charge.get(charge.id)
        assert charge.id
        assert charge.status == 'paid'
        charge.refund(10000)
        self.assertEqual(charge['status'], 'partially_refunded')
        charge.refund()
        self.assertEqual(charge['status'], 'refunded')
        retrieved_charge = self.client.Charge.get(charge.id)
        assert charge.id

    def test_02_cash_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.cash_charge_object)
        assert charge.id

    def test_03_bank_charge_done(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        charge = self.client.Charge.create(self.bank_charge_object)
        assert charge.id

    def test_04_card_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.card_charge_object)

    def test_05_cash_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.cash_charge_object)

    def test_06_bank_charge_authentication_fail(self):
        self.client.api_key = ''
        self.assertRaises(self.client.ConektaError, self.client.Charge.create, self.bank_charge_object)

    def test_07_log_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        logs = self.client.Log.where({})
        self.assertIsInstance(logs[0], self.client.Log)
        retrieved_log = self.client.Log.get(logs[0].id)
        assert retrieved_log.id

    def test_08_event_complete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        events = self.client.Event.where({})
        self.assertIsInstance(events[0], self.client.Event)
        retrieved_event = self.client.Event.get(events[0].id)
        assert retrieved_event.id

    def test_09_plan_create(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        plan = self.client.Plan.create(self.plan_object)
        assert plan.id == self.plan_object['id']
        plan = self.client.Plan.get(plan.id)
        assert plan.id == self.plan_object['id']

    def test_10_customer_create(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.create(self.customer_object)
        assert customer.name == self.customer_object['name']

    def test_11_cards(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.where({})[0]
        card = customer.createCard({'token_id':'tok_test_visa_4242'})
        assert card.last4 == '4242'
        card.update({'token_id':'tok_test_mastercard_5100'})
        assert card.last4 == '5100'
        card.update({'active':False})
        assert card.active == False
        card.delete()
        assert card.deleted

    def test_12_subscription(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.where({})[0]
        subscription = customer.subscription
        if customer.subscription is None:
            subscription = customer.createSubscription({'plan_id':self.plan_object['id']})
        assert subscription.id
        subscription.pause()
        assert subscription.status == 'paused'
        subscription.resume()
        assert subscription.status == 'active'
        subscription.cancel()
        assert subscription.status == 'canceled'

    def test_13_customer_delete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        customer = self.client.Customer.where({})[0]
        customer.delete()
        assert customer.deleted

    def test_14_plan_delete(self):
        self.client.api_key = '1tv5yJp3xnVZ7eK67m4h'
        plan = self.client.Plan.get(self.plan_object['id'])
        plan.delete()
        assert plan.deleted

