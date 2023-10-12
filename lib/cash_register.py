#!/usr/bin/env python3

class CashRegister:
  

  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.prev_trans = []


  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)
    self.prev_trans.append({"item": item, "price": price, "quantity": quantity})


  def apply_discount(self):
    if self.discount:
      self.total -= int(self.total * self.discount / 100)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")


  def void_last_transaction(self):
    if not self.prev_trans:
      print("There are no transactions to void.")
    self.total -= self.prev_trans[-1]["price"] * self.prev_trans[-1]["quantity"]
    for _ in range(self.prev_trans[-1]["quantity"]):
      self.items.pop()

    self.prev_trans.pop()