class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self,amount, desc=""):
        self.ledger.append({"amount":amount,"description":desc})
        self.balance += amount

    def withdraw(self,amount, desc=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":desc})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budgetCategory):
        if (self.check_funds(amount)):
            self.withdraw(amount,f"Transfer to {budgetCategory.name}")
            budgetCategory.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True

    def __str__(self):
        ledgerStr = self.name.center(30,'*')
        ledgerStr += "\n"
        for i in self.ledger:
            ledgerStr += i["description"][0:23].ljust(23," ")+str(format(i["amount"],".2f")).rjust(7," ")+"\n"
            ledgerStr += f"Total: {str(self.balance)}"
        return ledgerStr


def create_spend_chart(*categories):
    spendingDict = {}
    percentageDict = {}
    totalSpent = 0
    for l in categories:
        for i in l:
            spendingDict[i.name] = 0
            for k in i.ledger:
            if float(k["amount"]) < 0:
                spendingDict[i.name] = abs(k["amount"]) + spendingDict[i.name]
    totalSpent = sum(spendingDict.values())
    for key in spendingDict:
        percentageDict[key] = (spendingDict[key]/totalSpent)*100
    barChartStr = "Percentage spent by category\n"
    for i in range(100,-10,-10):
        barChartStr += f"{i}|".rjust(4," ")
        for keys in percentageDict:
            if i < percentageDict[keys]:
                barChartStr += " o "
            elif i > percentageDict[keys]:
                barChartStr += "   "
        barChartStr += "\n"
    barChartStr += "    ".ljust((len(percentageDict)*3)+5,"-")
    barChartCategories = "\n"
    for i in range(0,max(len(x)for x in spendingDict)):
        barChartCategories += "     "
        for key in spendingDict:
            if i < len(key):
                barChartCategories += key[i]+"  "
            else:
                barChartCategories += "   "
        if i != max(len(x)for x in spendingDict)-1:
            barChartCategories += "\n"
    barChartStr += barChartCategories
    return barChartStr
