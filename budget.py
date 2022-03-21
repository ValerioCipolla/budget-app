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
  total_spent = 0
  for category in categories:
    for entry in category.ledger:
      if entry["amount"] < 0:
        total_spent += entry["amount"] * -1
  spending_dict = dict()
  for category in categories:
    spending_dict[category.category] = 0
    for entry in category.ledger:
      if entry["amount"] < 0:
        spending_dict[category.category] += entry["amount"] * -1
  percentages_spending = []
  for v in spending_dict.values():
    percentages_spending.append(int((v * 100) / total_spent))
  result = ""
  result += f"Percentage spent by category\n100|{add_o(percentages_spending, 100)}\n 90|{add_o(percentages_spending, 90)}\n 80|{add_o(percentages_spending, 80)}\n 70|{add_o(percentages_spending, 70)}\n 60|{add_o(percentages_spending, 60)}\n 50|{add_o(percentages_spending, 50)}\n 40|{add_o(percentages_spending, 40)}\n 30|{add_o(percentages_spending, 30)}\n 20|{add_o(percentages_spending, 20)}\n 10|{add_o(percentages_spending, 10)}\n  0|{add_o(percentages_spending, 0)}\n"
  result += ""
  result += "    " + "---" * len(categories) + "-\n    "
  categories_max_length = max(list(map(lambda x: len(x.category),categories)))
  strings_to_add = list(map(lambda x: x.category.ljust(categories_max_length), categories))
  character_index = 0
  for n in range(categories_max_length):
    string_index = 0
    for m in range(len(categories)):
      result += f" {strings_to_add[string_index][character_index]} "
      string_index += 1
    result += " \n    "
    character_index += 1
  result = result.rstrip() + "  "
  return result

def add_o(percentages_list, ceiling):
  result = ""
  for percentage in percentages_list:
    if percentage < ceiling:
      result += "   "
    else:
      result += " o "
  result += " "
  return result
