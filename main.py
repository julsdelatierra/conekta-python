#!/usr/bin/python
# coding:utf-8

from conekta import Conekta

if __name__ == '__main__':
    client = Conekta()
    print client.products()