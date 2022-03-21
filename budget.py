class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": (amount * -1), "description": description})
      return True
    else:
      return False
      

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

  def __str__(self):
    result = self.category.center(30, "*")
    for entry in self.ledger:
      result += "\n"
      result += f"{entry['description'][0:23]:<23}"
      result += f"{'{:.2f}'.format(entry['amount'])[0:7]:>7}"
    total = 0
    for entry in self.ledger:
      total += entry["amount"]
    result += "\n"
    result += f"Total: {total}"
    return result




def create_spend_chart(categories):
  return 1

food = Category("Food")
clothing = Category("Clothing")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
food.transfer(50, clothing)

print(food)
print(clothing)
