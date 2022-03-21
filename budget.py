class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      return False
    else:
      self.ledger.append({"amount": (amount * -1), "description": description})
      return True

  def get_balance(self):
    current_balance = 0
    for entry in self.ledger:
      current_balance += entry["amount"]
    return current_balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.category}")
      category.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    else:
      return False




def create_spend_chart(categories):
  return 1

food = Category("Food")
clothing = Category("Clothing")
food.deposit(1000, "initial deposit")
food.transfer(2000, clothing)
print(food.ledger)
print(food.get_balance())
print(clothing.get_balance())
print(clothing.ledger)
print(food.check_funds(4000))
