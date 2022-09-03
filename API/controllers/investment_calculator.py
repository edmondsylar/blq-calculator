

# Daily total profit 5.26.
class BLQ_Investment_Calculator_v001:
    def __init__(self, investment, period, morning_percentage_profit):
        # our dily profit margin is 5.26
        # this means that the morning percentage given can help use calculate the 
        # evening percentage profit.

        # initialize investment and period neaded.
        self.principle_investment = investment
        self.investment_period = period

        # let's create the account balance
        self.account_balance = self.principle_investment

        # define the system variables.
        self.morning_percentage_profit = 0
        self.evening_percentage_profit = 0
        self.fixed_percentage_profit = 5.26
        
        # let's keep track of how much you make in the day 
        # evening vs morning.
        self.morning_profit = 0;
        self.evening_profit = 0

        # initialize the investment calculation
        self.__initialize(morning_percentage_profit)

        print("the loop is below ")

        # we can trigger or trade from hee.
        for i in range(0, self.investment_period):
            self.Trade()
            # print("Day: {}".format(i+1))



    def __initialize(self, morning_percentage_profit):
        # let's initialize the required variables.
        # we need to convest all system variables into 
        # actual percentages and round off the figures to 2 decimal places.
        
        self.morning_percentage_profit = (morning_percentage_profit/100)
        self.evening_percentage_profit = ((5.26/100 )- self.morning_percentage_profit)

        # return something.
        return True 


    def Trade(self):
        # get the morning profi.
        self._morning_profit() #we have gotten the morning profist
        # get evening Porfit
        self._evening_profit() #we have gotten the evening profits        
        pass


    # morning Profit 
    def _morning_profit(self):
        # calculate the morning profit.
        morning_profit = (self.account_balance*self.morning_percentage_profit)
        # let's compute the new account balance.
        self.account_balance += morning_profit
        # Assign new value to mornig profit variable. 
        self.morning_profit = morning_profit
        return True



    # evening profit.
    def _evening_profit(self):
        # get the evening profit
        evening_profit = (self.account_balance * self.evening_percentage_profit)
        # compute new account balance.
        self.account_balance += evening_profit
        # assign new evening profit
        self.evening_profit = evening_profit
        return True

    def get_report(self):
        # lets genrate a simple report.
        print ("\nPrinciple Investment: {:,} \nMorning Profit: {:,} \nEvening Profit: {:,} \n\nAccount Balance: {:,}"
        .format(round(self.principle_investment, 2), round(self.morning_profit,2), round(self.evening_profit, 2), round(self.account_balance, 2)))

    def _calculated_period(self, morning_percentage_profit):
        for i in range(0, self.investment_period):
            self.__initialize(morning_percentage_profit)
            # complete the iteration
        self.get_report()
        return True
        
    # def profit_calculator

# myAccount = BLQ_Investment_Calculator_v001(43608.28, 5, 2.26)
myAccount = BLQ_Investment_Calculator_v001(200000, 30, 2.26)
myAccount.get_report()


# if __name__ == '__main__':
#     # loop get nulpile user inputs
#     while True:
#         invenstment = float(input("Enter investment: "))
#         period = float(input("Enter investment period: "))
#         morning_percentage = float(input("Enter Morning percentage: "))

#         myAccount = BLQ_Investment_Calculator_v001(invenstment, period, morning_percentage)
#         myAccount.get_report()

