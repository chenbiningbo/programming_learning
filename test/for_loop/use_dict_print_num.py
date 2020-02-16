numbers = input("phone: ")
digtal_converter = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output =""
for number in numbers:
    output += digtal_converter.get(number) + " "
print(output)