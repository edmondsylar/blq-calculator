# BLQ Investiment application

mrn_percentage = (2.5/100)
evening_percentage = (3.2/100)
profit = 0;

# account_balance = 50000

def get_balance():
    print(account_balance)

def get_morning_profit(account_balance):
    profit = account_balance * mrn_percentage
    return profit

def get_evening_profit(account_balance):
    profit = account_balance * evening_percentage
    return profit

def consolidated_profit(account_balance):
    consolidated_profit = get_evening_profit(account_balance) + get_morning_profit(account_balance)
    # print(consolidated_profit)
    return consolidated_profit


def balance_plus_consolidated_profit(account_balance):
    tt_balance = account_balance + consolidated_profit(account_balance)
    return(tt_balance)

# check the consolidated profits.
# balance_plus_consolidated_profit()


acc_bal = 0

while True:
    # get the investiment capital
    account_bal = float(input("Investiment Amount:"))
    period = int(input("Period (Months): "))

    for i in range(0, period):
       acc_bal += account_bal
       checkout = balance_plus_consolidated_profit(acc_bal)
    #    print(checkout, "> Profits Day: ", i+1)
       
    print(acc_bal)
