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

customer = conekta.Customer(
    name="Gilberto Gil",
    email="gil.gil@mypayments.mx",
    phone=5567942342,
    street1="Jiminez 11",
    street2="Despacho 99",
    street3="La Condesa",
    city="Cuauhtemoc",
    state="DF",
    country="MX",
    zip="06100"
)

bank = conekta.Banks(type="banorte")

charge = conekta.Charge.create(
    amount=10000,
    currency="MXN",
    description="DVD - Zorro",
    customer=custome,
    bank=bank
)

print charge.parseJSON()

```

Charge via card

```python
import conekta

conekta.api_key = 'blablabla'

customer = conekta.Customer(
    name="Gilberto Gil",
    email="gil.gil@mypayments.mx",
    phone=5567942342,
    street1="Jiminez 11",
    street2="Despacho 99",
    street3="La Condesa",
    city="Cuauhtemoc",
    state="DF",
    country="MX",
    zip="06100"
)

card = conekta.Cards(
  name="Gilberto Gil",
  cvc="000",
  number="4111111111111111",
  exp_month="04",
  exp_year="16",
  success_url="https://www.ftw.com",
  failure_url="https://www.epic-fail.com"
)

charge = conekta.Charge.create(
    amount=10000,
    currency="MXN",
    description="DVD - Zorro",
    customer=custome,
    card=card
)

print charge.parseJSON()
```

Charge via oxxo

```python
import conekta

conekta.api_key = 'blablabla'

customer = conekta.Customer(
    name="Gilberto Gil",
    email="gil.gil@mypayments.mx",
    phone=5567942342,
    street1="Jiminez 11",
    street2="Despacho 99",
    street3="La Condesa",
    city="Cuauhtemoc",
    state="DF",
    country="MX",
    zip="06100"
)

bank = conekta.objects.Cash(type="oxxo")

charge = conekta.Charge.create(
    amount=10000,
    currency="MXN",
    description="DVD - Zorro",
    customer=custome,
    bank=bank
)

print charge.parseJSON()
```

## Endpoints

```
conekta.Charge.create()
```

## Clases

```
conekta.Charges
conekta.Cash
conekta.Banks
conekta.Cards
conekta.Customers
```
