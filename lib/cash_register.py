#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0) -> None:
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_price = 0

    def add_item(self, item_name, price, quantity=1):
        for i in range(quantity):
            self.items.append(item_name)
        self.total += price * quantity
        self.last_price = price * quantity

    def apply_discount(self):
        if self.total:
            self.total -= self.total * self.discount / 100
            print(f'After the discount, the total comes to ${int(self.total)}.')
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        self.items.pop()
        self.total -= self.last_price

    