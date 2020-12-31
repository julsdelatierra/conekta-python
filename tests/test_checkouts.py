#!/usr/bin/python
#coding: utf-8
#(c) 2020 Erick Colin <@erickcolin>

from . import BaseEndpointTestCase

class CheckoutsEndpointTestCase(BaseEndpointTestCase):

    def test_01_create_checkout(self):
        
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object.copy())

        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.status != "Issued"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36
    
    def test_02_create_checkout_recurrent(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object_multiple.copy())

        assert checkout.recurrent == True
        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36

    
    def test_03_create_checkout_msi(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object_msi.copy())

        assert checkout.monthly_installments_enabled == True
        assert checkout.type == "PaymentLink"
        assert checkout.object == "checkout"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36

    def test_04_create_checkout_redirect(self):
        
        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'

        checkout = self.client.Checkout.create(self.checkout_object.copy())

        assert checkout.type == "checkout"
        assert checkout.object == "checkout"
        assert checkout.status != "Issued"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36


    def test_05_create_checkout_msi_type_checkout(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.create(self.checkout_object_type_checkout.copy())

        assert checkout.monthly_installments_enabled == True
        assert checkout.type == "checkout"
        assert checkout.object == "checkout"
        assert checkout.url.startswith("https:\\pay.conekta")
        assert checkout.id.len() == 36

    
    def test_06_checkout_sendmail(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.sendEmail(self.checkout_object_send.copy())

        assert isinstance(checkout,self.checkout_object_send.copy())

    def test_07_checkout_sendsms(self):

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.sendSms(self.checkout_object_send.copy())

        assert isinstance(checkout,self.checkout_object_send.copy())

    def test_08_checkout_cancel():

        self.client.api_key = 'key_ZLy4aP2szht1HqzkCezDEA'
        checkout = self.client.Checkout.cancel(self.checkout_object_send.copy())

        assert checkout.status == "Cancelled"