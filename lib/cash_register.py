#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.total = 0
        self.items = []
        self.previous_transactions = []

        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.items:
            print("There is no discount to apply.")
            return

        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()

        item = transaction["item"]
        price = transaction["price"]
        quantity = transaction["quantity"]

        self.total -= price * quantity

        for _ in range(quantity):
            self.items.remove(item)