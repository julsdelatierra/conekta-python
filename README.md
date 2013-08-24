Conekta
=========

Wrapper for api.conekta.io

Install

```sh
pip install conekta
```

```sh
easy_install conekta
```


Charge via bank:

```python
import conekta

conekta.api_key = 'blablabla'

var data = {
    "amount": 10000,
    "currency": "MXN",
    "description": "DVD - Zorro",
    "customer": {
        "name": "Gilberto Gil",
        "email": "gil.gil@mypayments.mx",
        "phone": 5567942342,
        "street1": "Jiminez 11",
        "street2": "Despacho 99",
        "street3": "La Condesa",
        "city": "Cuauhtemoc",
        "state": "DF",
        "country": "MX",
        "zip": "06100"
    },
    "bank": {
        "type": "banorte"
    }
}

charge = conekta.Charge.create(data)

print charge.parseJSON()

```

Charge via card

```python
import conekta

conekta.api_key = 'blablabla'

var data = {
    "amount": 10000,
    "currency": "MXN",
    "description": "DVD - Zorro",
    "customer": {
        "name": "Gilberto Gil",
        "email": "gil.gil@mypayments.mx",
        "phone": 5567942342,
        "street1": "Jiminez 11",
        "street2": "Despacho 99",
        "street3": "La Condesa",
        "city": "Cuauhtemoc",
        "state": "DF",
        "country": "MX",
        "zip": "06100"
    },
    "card": {
        "name": "Gilberto Gil",
        "cvc": "000",
        "number": "4111111111111111",
        "exp_month": "04",
        "exp_year": "16",
        "success_url": "https://www.ftw.com",
        "failure_url": "https://www.epic-fail.com"
    }
}

charge = conekta.Charge.create(data)

print charge.parseJSON()
```

Charge via oxxo

```python
import conekta

conekta.api_key = 'blablabla'

var data = {
    "amount": 10000,
    "currency": "MXN",
    "description": "DVD - Zorro",
    "customer": {
        "name": "Gilberto Gil",
        "email": "gil.gil@mypayments.mx",
        "phone": 5567942342,
        "street1": "Jiminez 11",
        "street2": "Despacho 99",
        "street3": "La Condesa",
        "city": "Cuauhtemoc",
        "state": "DF",
        "country": "MX",
        "zip": "06100"
    },
    "cash": {
        "type": "oxxo"
    }
}

charge = conekta.Charge.create(data)

print charge.parseJSON()

#Also you can get the attributes from the conekta response class:
print charge.id

#Or if you get an error:
print charge.error.type
```

#Retrieve event info

```python
import conekta

conekta.api_key = 'blablabla'

event = conekta.Event.retrieve('521701ee19cbbea233000091')

print event.parseJSON()

#Also you can get the attributes from the conekta response class:
print event.id

#Or if you get an error:
print event.error.type
```

## Endpoints

```
conekta.Charge.create()
conekta.Event.retrieve()
```

## Tests

You can test the conekta library with nose on the conekta library root:

```sh
$ nosetests
```
