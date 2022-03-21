class Category:
  ledger = []

  def __init__(self, category):
    self.category = category

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    self.ledger.append({"amount": (amount * -1), "description": description})



def create_spend_chart(categories):
  return 1

app = Category("food")
app.deposit(100, "apples")
app.deposit(2, "apples")
app.withdraw(14, "disco")
print(app.ledger)