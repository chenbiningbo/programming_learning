info = [ "TUR2000ESP",  "CHL7800GRC",  "COL1100USA",  "TWN7300MAR",  "ARG1528BOL",  "IND4300NOR" ]
# Dictionary with country codes
countries = { "TUR": "Turkey", "ESP": "Spain", "CHL": "Chile", "GRC": "Greece", "COL": "Colombia", \
        "USA": "USA", "TWN": "Taiwan", "MAR": "Morocco", "ARG": "Argentina", "BOL": "Bolivia", \
        "IND": "India", "NOR": "Norway" }
#-------------------  Part of the problem, do not delete ------------------------------#

# Start writing your code below:
count = 1
for contract in info:
    start = contract[:3]
    distance = contract[start]
    end = contract[-3:]
    print('Contract ' + str(count) + ': from'+ countries[start] +'to'+ countries[end]+'travelling' + distance+ 'miles')
    count +=1