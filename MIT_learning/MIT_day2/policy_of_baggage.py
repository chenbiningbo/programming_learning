BaggageNum = int(input('Please input the num of Baggage:'))
Cost = 36
Rate = 1
counter = 1
if BaggageNum <=1:
    print('The first checked bag is free of charge')
elif BaggageNum > 1:
    while counter < BaggageNum-1:
        Rate *= 1.2
        Cost = Cost +Cost*Rate
        counter += 1
    print('the all cost is:', round(Cost,3))