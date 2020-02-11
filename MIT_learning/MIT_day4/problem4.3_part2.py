
#---------------Part of the question do not modify---------------#
Age_of_Customers = [45, 62, 36, 40, 50, 20, 39, 54, 16, 60, 56, 46, 52, 28, 31, 27, 66, 69, 59, 49, 47, 44, 37, 18, 38]
#----------------------------------------------------------------#

# Create a function that goes through a list and returns the index of the element with the highest value.
# ---> Write your answer below
def get_index_of_max_age(ages):
    max_age = max(ages)
    return ages.index(max_age)+1

# Using the function you just created, in one line of code, print the maximum age from the list Age_of_Customers
# ---> write your answer below
print('the max age of the customers list is  '+ str(max(Age_of_Customers)) + ' years old')
print('the index of the max age customers is the number: '+ str(get_index_of_max_age(Age_of_Customers)))