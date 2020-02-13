numbers = [1,2,3,4,5,3,2,6,8,6,8,4,3]
new_list =[]

for number in numbers:
    if number not in new_list:
        new_list.append(number)
print(new_list)