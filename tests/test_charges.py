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

    def test_plan_create(self):
        plan = self.client.Plan.create(self.plan_object)
        assert plan.id == self.plan_object['id']

    def test_customer_create(self):
        customer = self.client.Customer.create(self.customer_object)
        assert customer.name == self.customer_object['name']

    def test_cards(self):
        customer = self.client.Customer.all()[0]
        card = customer.createCard({'token_id':'tok_test_visa_4242'})
        assert card.last4 == '4242'
        card.update({'active':False})
        assert card.active == False
        card.update({'token_id':'tok_test_mastercard_5100'})
        assert card.last4 == '5100'
        card.delete()
        assert card.deleted

    def test_subscription(self):
        customer = self.client.Customer.all()[0]
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

    def test_customer_delete(self):
        customer = self.client.Customer.all()[0]
        customer.delete()
        assert customer.deleted

    def test_plan_delete(self):
        plan = self.client.Plan.retrieve(self.plan_object['id'])
        plan.delete()
        assert plan.deleted

