#---------------Part of the question do not modify---------------#
Age_of_Customers = [45, 62, 36, 40, 50, 20, 39, 54, 16, 60, 56, 46, 52, 28, 31, 27, 66, 69, 59, 49, 47, 44, 37, 18, 38]
#----------------------------------------------------------------#

# Write a for loop for that goes through the list Age_of_Customers and prints the first element
# that is smaller than 19 along with its index. Also stop the loop immediately after the print.
# ---> Write your answer below
for age in Age_of_Customers:
    if age <19:
        print('the first element that is smaller than 19 age is '+ str(age)+ ' years old')
        print('the index is: ' + str(Age_of_Customers.index(age)))
        break

# Using a while loop count the number of customers older than 50 and print the final number.
# ---> Write your answer below
index = 0
count = 0
while index<len(Age_of_Customers):
    if Age_of_Customers[index]>50:
        count +=1
    index +=1
print('older than 50 number is: ' + str(count))