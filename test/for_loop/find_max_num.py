def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

numbers = [3, 5, 2, 7, 10, 8, 7]
print(find_max(numbers))
