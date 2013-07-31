pyconekta
=========

Install

```sh
pip install conekta
```

```sh
easy_install conekta
```

Wrapper for conekta.mx


For example:

```python
from conekta import Conekta

client = Conekta(public_key='asdasd', private_key='asdasd')

data = {
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

oxxo_charge = client.charges.create(data)

print oxxo_charge.to_json()

```

## Endpoints

```
charges.create()
```
