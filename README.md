pyconekta
=========

Wrapper for conekta.mx


For example:

```python
from conekta import Conekta

client = Conekta()

products = client.products()

for product in products:
    print product

```

## Endpoints

```
products()
products.add()

orders()
orders.add()

suscriptions()
suscriptions.add()

companies()
companies.add()
```
