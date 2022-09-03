# let's creata class called Account.

class BLQ_InvestmentCalaculator:
    def __init__(self, inventiment):
        # initialize the value of investiment.
        self.inventiment = inventiment
        self.avg_daily_profit = 0.05
        self.account_balance = self.inventiment 

        # avg_monthly_profit
        # we are standardizing the number of days in a month to 30 in a 
        # month
        self.avg_monthly_profit = self.avg_daily_profit * 30

        # this is going to be our standard period in months.
        self.std_period = 2

    def _daily_profit(self, balance):
        d_profit = balance * self.avg_daily_profit
        return  d_profit

    def _calculate_monthly_profit(self):
        # this is our number of days in a month
        num_days = 30
        account_balance = self.inventiment
        # self.account_balance = self.inventiment
        for each_day in range(0, num_days):
            day_one_proft = self._daily_profit(account_balance)
            account_balance += day_one_proft

            # print("Day: {} \nProfit:  {} \nFinal Balance: {}".format(each_day+1, day_one_proft, account_balance))
            # break
        # print("Monthly Balance: {:,}".format(round(account_balance, 2)))
        return account_balance

    def _weekly_profit(self):
        weekly_balance = self._calculate_monthly_profit()/4
        # print("Weekly Balance :", str(weekly_balance))
        # print("Weekly Balance: {:,}".format(round(weekly_balance, 2)))
        return weekly_balance

