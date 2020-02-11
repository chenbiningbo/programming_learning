Shoes = {0 : ["Running",14,3],1 : ["Running",13.5,5], 2 : ["Running",9,8], 3: ["Running" ,13,8],
         4:["Strenght Training",11 ,8], 5:["Strenght Training",10.5,1], 6:["Strenght Training",7.5,7],
         7:["Strenght Training",10,1], 8:["Strenght Training",8.5,2], 9:["Running",11.5,9],
         10:["Strenght Training",9,8], 11:["Strenght Training",11,3], 12:["Strenght Training",8,3],
         13:["Running",6.5,2], 14:["Running",10.5,7], 15:["Strenght Training",12,3],
         16:["Running",8,0],17:["Strenght Training",12,4], 18:["Strenght Training",7,9],
         19:["Strenght Training",9.5,7], 20:["Running",12.5,0],21:["Strenght Training",7,9]}

list_R = []
list_ST = []

for value in Shoes.values():
    if value[0] == 'Running':
        list_R.append(value)
    else:
        list_ST.append(value)
print(list_ST)
print(list_R)

final_list_R = []
for item in list_R:
    final_list_R.append(item[1:])
print(final_list_R)
print('')
print('')
print('')
print('')

final_list_R.sort(key=lambda x:x[0], reverse=False)
print(final_list_R)