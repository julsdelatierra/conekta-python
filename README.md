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

Charge via card

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

var data = {
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

charge = conekta.Charge.create(data)

#Also you can get the attributes from the conekta response class:
print charge.id

#Or if you get an error:
try:
    #your code
catch ConektaError:
    print 'Exception in code'

```

Charge via oxxo

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

var data = {
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

charge = conekta.Charge.create(data)

#Also you can get the attributes from the conekta response class:
print charge.id

#Or if you get an error:
try:
    #your code
catch ConektaError:
    print 'Exception in code'
```

Charge via bank:

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

var data = {
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

charge = conekta.Charge.create(data)

#Also you can get the attributes from the conekta response class:
print charge.id

#Or if you get an error:
try:
    #your code
catch ConektaError:
    print 'Exception in code'

```


#Retrieve events

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

events = conekta.Event.all()

```

## Endpoints

```
conekta.Charge.create()
conekta.Charge.all()
conekta.Charge.retrieve('charge_id')
charge.refund(amount)
conekta.Event.all()
conekta.Event.retrieve('event_id')
conekta.Log.all()
conekta.Log.retrieve('log_id')
```

## Tests

You can test the conekta library with nose on the conekta library root:

```sh
$ nosetests
```
