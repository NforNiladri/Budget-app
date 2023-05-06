class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.category)
            category.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    # Create a list of category names and a list of withdrawal amounts for each category
    category_names = []
    withdrawal_amounts = []
    for category in categories:
        category_names.append(category.category)
        withdrawals = 0
        for item in category.ledger:
            if item['amount'] < 0:
                withdrawals += abs(item['amount'])
        withdrawal_amounts.append(withdrawals)

    # Calculate the total withdrawal amount
    total_withdrawals = sum(withdrawal_amounts)

    # Calculate the percentage spent in each category
    percentages = []
    for amount in withdrawal_amounts:
        percentage = amount / total_withdrawals * 100
        percentages.append(int(percentage))

    # Create the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find the length of the longest category name
    max_length = max([len(name) for name in category_names])

    # Add the category names to the chart
    for i in range(max_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n"

    return chart
