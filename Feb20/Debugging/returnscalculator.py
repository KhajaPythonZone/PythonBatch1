import pdb

invested_amount = int(input('Enter your invested amount = '))
return_amount = int(input('Enter the amount returned from investment = '))
months_count = int(input('Enter number of months it took for return = '))
# pdb.set_trace()
profit = return_amount - invested_amount
print(f"Absolute profit/loss is {profit} $")
net_profit_per_month = profit/months_count
avg_profit_per_month = (net_profit_per_month * 100/invested_amount)
print(f'Return % per month is {avg_profit_per_month}')
yearly_profit = avg_profit_per_month * 12
print(f'Return % per year is {yearly_profit}')