#!/usr/bin/python
#coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import unittest

from conekta import Conekta

class BaseEndpointTestCase(unittest.TestCase):

  api = Conekta()

  default_product_id = ''
  default_product_object = {}
  default_order_id = ''
  default_order_object = {}
  default_suscription_id = ''
  default_suscription_object = {}

