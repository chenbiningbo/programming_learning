# Problem 5
'''
HSBD Bank has hired Mario, a data analyst, to do some data analysis to help the company
to better understand the customers' demographic characteristics. The upper management
has some questions, and Mario must find the answer by analyzing the data available.

To start, please run the cell below to get the data provided by the bank (it might take a few seconds to finish running).
'''
# Run this cell but DO NOT MODIFY
# Do not modify this part, it belongs to the question
#------------------------------------------------------------------------------------------------------------------
import pandas as pd
url='https://raw.githubusercontent.com/juliencohensolal/BankMarketing/master/rawData/bank-additional-full.csv'
data = pd.read_csv(url,sep=";") # use sep="," for coma separation.
Age = data['age']
data = data[['age', 'job', 'marital']].copy()
#------------------------------------------------------------------------------------------------------------------

data.to_csv("../Problem/pro_data.csv")
'''
The series Age (defined in the cell above) contains information about the customers' age.

Write a script that prints the customers' age every 5,000th customers. 
This means printing the value associated to the 5,000th element in 
the series, the 10,000th element, the 15,000th element, and so on.

'''
# Write your script for 5.1 here
total_count = Age.count()
i=5000
while i < total_count:
    print('The age of the '+str(i)+' th customer is '+str(Age.iloc[i]))
    i+=5000

#5.2
# Print the name of all the columns in the dataframe
print(data.columns.values)
# Print the shape of the dataframe to understand the size of data
print(data.shape)
# In one line of code, print the average, the median, the maximum and the minimum age of the customers.
print('average Age:'+str(Age.mean())+' median Age: '+str(Age.median())+' max Age: '+str(Age.max())+'min Age:'+str(Age.min()))


#5.3
# Create a new column called normalized_age that contains the age of each customer divided by the maximum age.
max_age = Age.max()
data['normalized_age'] = data.apply(lambda x : x.age/max_age, axis=1)

# Print the job information for all customers between index 500 and index 515 (including 500 and 515).
for i in range(500,516):
    customer = data.iloc[i]
    print(str(i)+'  '+customer.job)
# Delete the marital column from the dataframe
data6 = data.drop(columns=['marital'])
print(data6)

# Save the dataframe as an excel file to your local computer and name it Problem5.
# FIX_ME
data6.to_csv('../Problem/Problem5.csv')