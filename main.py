#!/usr/bin/python
# coding:utf-8

from conekta import Conekta

if __name__ == '__main__':
    client = Conekta()
    '''
    print client.products()
    print client.orders()
    print client.suscriptions()
    '''
    '''
    print client.orders.add(params={
        "shipment": {
            "address": {
                "line_1": "panuco",
                "line_2": "65",
                "colonia": "polanco",
                "city": "monterrey",
                "state": "nuevo leon",
                "country": "Mexico",
                "postal_code": "55555",
                "phone": "81836358618",
                "email": "julian@lastroom.mx",
                "name": "legendario"
            },
            "price": "100.0",
            "carrier": "Estafeta Terrestre",
            "service_name": "terrestre",
            "service_code": "Estafeta Terrestre"
        },
        "payment": {
            "type": "credit_card",
            "credit_card": {
                "name": "leo",
                "number": "4111111111111111",
                "cvv": "123",
                "exp_month": "12",
                "exp_year": "15"
            },
            "success_url": "http://lastroom.mx",
            "failure_url": "http://lastroom.mx",
            "billing_info": {
                "country": "MX",
                "city": "Mty",
                "colonia": "Florida",
                "email": "julian@lastroom.mx",
                "notorary": "28",
                "phone": "12345678",
                "postal_code": "12345",
                "rfc": "tcyuneuu3838",
                "state": "NL",
                "street": "sin salida",
                "line_1": "Florida",
                "line_2": "28"
            }
        },
        "items": [{
            "unit_price": "100.00",
            "quantity": "1"
        }]
    })
    '''
    '''
    client.suscriptions.add(params = {
        "total": "100.00",
        "shipment": {
            "address": {
                "line_1": "panuco",
                "line_2": "65",
                "colonia": "polanco",
                "city": "monterrey",
                "state": "nuevo leon",
                "country": "Mexico",
                "postal_code": "55555",
                "phone": "81836358618",
                "email": "legendary_hopper@miempresa.com",
                "name": "legendario"
            },
            "price": "100.0",
            "carrier": "Estafeta Terrestre",
            "service_name": "terrestre",
            "service_code": "Estafeta Terrestre",
            "period": {
                "length": "1",
                "unit": "days",
                "total_number": "3"
            }
        },
        "payment": {
            "type": "credit_card",
            "credit_card": {
                "name": "leo",
                "number": "4111111111111111",
                "cvv": "123",
                "exp_month": "12",
                "exp_year": "15"
            },
            "success_url": "http://ftw.com",
            "failure_url": "http://epic_fail.mx",
            "billing_info": {
                "country": "MX",
                "city": "Mty",
                "colonia": "Florida",
                "email": "legendary_hopper@hotmail.com",
                "notorary": "28",
                "phone": "12345678",
                "postal_code": "12345",
                "rfc": "tcyuneuu3838",
                "state": "NL",
                "street": "sin salida",
                "line_1": "Florida",
                "line_2": "28"
            },
            "period": {
                "length": "1",
                "unit": "days",
                "total_number": "3"
            }
        },
        "items": [{
            "unit_price": "100.00",
            "quantity": "1"
        }]
    })
    '''

    client.companies.add('2756617', {
        "company_config": {
            "fiscal_company_name": "My company inc",
            "fiscal_rfc": "BUGP8012315V3",
            "fiscal_address": "street",
            "fiscal_city": "my city",
            "fiscal_state": "my state",
            "fiscal_postal_code": "45678",
            "fiscal_telefono": "12345678",
            "tax_included_in_product_price": True,
            "show_tax_in_price": True,
            "tax_rate": 1.5,
            "conekta_shipping": True,
            "shipping_address": {
                "line_1": "panuco",
                "line_2": "65",
                "colonia": "polanco",
                "city": "monterrey",
                "state": "nuevo leon",
                "country": "Mexico",
                "postal_code": "55555",
                "phone": "81836358618",
                "email": "legendary_hopper@miempresa.com",
                "name": "legendario"
            }
        },
        "url": "https://mypage.com"
    })
    
