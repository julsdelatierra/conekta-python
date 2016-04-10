![alt tag](https://raw.github.com/conekta/conekta-python/master/readme_files/cover.png)

Conekta Python v 1.1.1
======================

Wrapper for api.conekta.io

##NOT SUPPORTED: If you want to implement conekta wrapper go to https://github.com/conekta/conekta-python


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
conekta.locale = 'es'

try:
  charge = conekta.Charge.create({
    "amount": 51000,
    "currency": "MXN",
    "description": "Pizza Delivery",
    "reference_id": "orden_de_id_interno",
    "card": request.POST["conektaTokenId"] 
    #request.form["conektaTokenId"], request.params["conektaTokenId"], "tok_a4Ff0dD2xYZZq82d9"
  })

except conekta.ConektaError as e:
  print e.message 
  #El pago no pudo ser procesado

#You can also get the attributes from the conekta response class:
print charge.id

#Or in the event of an error, you can expect a ConektaError to be raised
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

#Or in the event of an error, you can expect a ConektaError to be raised
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

#Or in the event of an error, you can expect a ConektaError to be raised
```

# Retrieve events

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'
events = conekta.Event.all()
```

## Endpoints

```python
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

License
-------
Developed by [Conekta](https://www.conekta.io). Available with [MIT License](LICENSE).

We are hiring
-------------

If you are a comfortable working with a range of backend languages (Java, Python, Ruby, PHP, etc) and frameworks, you have solid foundation in data structures, algorithms and software design with strong analytical and debugging skills. 
Send your CV, github to quieroser@conekta.io

