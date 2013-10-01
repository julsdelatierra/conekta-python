#!/usr/bin/python
# coding: utf-8
#(c) 2013 Julian Ceballos <@jceb>

import unittest

import conekta


class BaseEndpointTestCase(unittest.TestCase):

    client = conekta

    card_charge_object = {
        "description": "Grad Stogies: Second Class",
        "amount": 20000,
        "currency": "MXN",
        "reference_id": "9893-cohib_s1_wolf_pack",
        "card": {
            "number": 4111111111111111,
            "exp_month": 12,
            "exp_year": 2015,
            "name": "Thomas Logan",
            "cvc": 666,
            "address": {
                "street1": "250 Alexis St",
                "city": "Red Deer",
                "state": "Alberta",
                "country": "Canada",
                "zip": "T4N 0B8"
            }
        }
    }
    
    cash_charge_object = {
        "currency": "MXN",
        "amount": 20000,
        "description": "Grad Stogies: Second Class",
        "reference_id": "9893-cohib_s1_wolf_pack",
        "cash": {
            "type": "oxxo"
        },
        "details": {
            "name": "Wolverine",
            "email": "logan.thomas@xmen.org",
            "phone": "403-342-0642"
        }
    }
    
    bank_charge_object = {
        "currency": "MXN",
        "amount": 20000,
        "description": "Grad Stogies: Second Class",
        "reference_id": "9893-cohib_s1_wolf_pack",
        "bank": {
            "type": "banorte"
        },
        "details": {
            "name": "Wolverine",
            "email": "logan.thomas@xmen.org",
            "phone": "403-342-0642"
        }
    }
