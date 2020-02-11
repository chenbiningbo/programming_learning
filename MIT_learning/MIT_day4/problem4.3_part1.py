# Revenue is a list that contains the daily revenue for the last 7 days.
Revenue = [100, 200, 150, 70, 120, 230, 55]

# Cost is a list that contains the daily cost for the last 7 days.
Cost = [80, 95, 75, 70, 100, 130, 25]

profit = []
for i in range(0, 7):
    profit.append(Revenue[i]-Cost[i])
print(profit)

weekly_prfit = 0
for p in profit:
    weekly_prfit +=p
print(weekly_prfit)

