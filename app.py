

# create a class called Account.
class Account:
    def __init__(self, account_name, account_balance):
        self.account_name = account_name
        self.account_balance = account_balance

        # create 2 variables, the average 
        # morning percentage profit and the average evening percentage profit.
        self.avg_mng_percentage_profit = (2.5/100)
        self.avg_env_percentage_profit = (3.2/100)

    def _morning_profit(self):
        profit = self.account_balance * self.avg_mng_percentage_profit
        # lets update the account balance.
        self.account_balance + profit

        # return the profit        
        return profit 

    def _evening_profit(self):
        profit = self.account_balance * self.avg_env_percentage_profit
        # lets update the account balance.
        self.account_balance + profit

        # return the profit
        return profit

    def _consolidate_funds(self):
        morning_profit = self.account_balance * self.avg_mng_percentage_profit()

        print(morning_profit)




acc = Account("Edmond Musiitwa", 50000)
acc._consolidate_funds()