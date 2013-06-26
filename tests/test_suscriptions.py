#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

from . import BaseEndpointTestCase

class SuscriptionsEndpointTestCase(BaseEndpointTestCase):

  def test_get_suscriptions(self):
    response = self.api.suscriptions()
    print response
    assert True

  def test_get_suscription(self):
    response = self.api.suscriptions(self.default_suscription_id)
    print response
    assert 'items' in response

  def test_create_product(self):
    response = self.api.suscriptions.add(self.default_suscription_object)
    print response
    assert response['fraud_response'] == None
    assert error == null
