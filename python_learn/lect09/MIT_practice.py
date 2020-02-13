# end = 6
# counter = 1
# summray = 0
# while counter <= end:
#     summray = summray + counter
#     counter += 1
# print(summray)
#
#
#
# num = 0
# while num < 10:
#     num += 2
#     print(num)
# else:
#     print('Goodbye!')


# for count in range(2,12,2):
#     print(count)
# print('Goodbye!')

# print('Hello!')
# num = 12
# for count in range(5):
#     num -=2
#     print(num)


# print('Hello!')
# for i in range(10, 0, -2):
#     print(i)
#
#
# print('Hello!')
# for i in range(0, 10,2):
#     print(10 - i)


# end = 6
# counter = 1
# summray = 0
# while counter <= end:
#     summray = summray + counter
#     counter += 1
# print(summray)


# end = 6
# total = end
# for next in range(end):
#     total += next
# print(total)

"""
迭代演示，平方
"""

# x = int(input('please input a number:'))
# ans = 0
# itsleft = x
# while (itsleft != 0):
#     ans = ans + x
#     itsleft = itsleft - 1
# print(str(x) + '*' + str(x) + ' = ' + str(ans))


# num = 'sdf'
# for num in range(5):
#     print(num)
# print(num)

# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!')

# for letter in 'hola':
#     print(letter)

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# divisor = 2
# for num in range(0, 10, 2):
#     print(num/divisor)

# greeting = 'Hello!'
# count = 0
#
# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print(letter)
#     print(letter)
#
# print('done')


# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1
#
# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons))
"""
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
"""

# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " +


# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break

# #
#
# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     while True:
#         count += len(phrase)
#         break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))


# count = 0
# # phrase = "hello, world"
# # for iteration in range(5):
# #     count += len(phrase)
# #     print("Iteration " + str(iteration) + "; count is: " + str(count))


# !/usr/bin/env python
# coding=utf-8

# from pyecharts.charts import Bar  # 导入第三方库
#
# def()
# # attr = ["{}day".format(i) for i in range(1, 8)]    #这样的话X坐标就是1day、2day、3day...
# attr = ["Mon", "Feb", "Wed", "Thu", "Fri", "Sat", "Sun"]  # 这样X坐标就是星期
# v1 = [1.49, 2.09, 4.03, 2.23, 5.26, 7.71, 7.56]
# v2 = [0.3, 0.9, 0.2, 0.4, 0.7, 0.7, 0.6]
# v3 = [18.15, 13.22, 11.28, 17.99, 18.7, 19.7, 15.6]
#
# bar = Bar("XXX情况总览", "本图表展示过去一周的ABC情况")  # 这里是主标题和副标题
# bar.add("A值", attr, v1, mark_line=["average"], mark_point=["max", "min"])  # 每一个值的名称以及要展现平均值和最大最小值
# bar.add("B值", attr, v2, mark_line=["average"], mark_point=["max", "min"])
# bar.add("C值", attr, v3, mark_line=["average"], mark_point=["max", "min"])
#
# bar.render('/tmp/111.html')  # 在/tmp文件夹里生成一个111.html文件

# s = input('please input s string:')
# counts = 0
# # s = 'azcsdfasbobobegghakl'
# for letter in s:
#     if letter in ['a', 'e', 'i', 'o', 'u']:
#         counts += 1
# # print('Number of vowels: {}'.format(counts))
# print('Number of vowels: ' + str(counts))

# s = 'afdsiohngfdsa'
# counts = 0
# for letter in s:
#     if letter in ['a', 'e', 'i', 'o', 'u']:
#         counts += 1
# print('Number of vowels:' + ' ' + str(counts))

# s = 'azcbobobegghakl'
# s1 = s
# arr = ['a', 'e', 'i', 'o', 'u']
# for t in arr:
#     s1 = s1.replace(t, "")
# print('Number of vowels: ' + str(len(s) - len(s1)))

# s = 'azcbobobegghakl'
# t = 'bob'
# count = 0
# i = 0
# while i <= len(s) - len(t):
#     idx = s.find(t, i, i + len(t))
#     if idx > -1:
#         count += 1
#     i += 1
# print('Number of times bob occurs is: ' + str(count))

# s = 'azcbobobegghakl'
# arr = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for t in arr:
#     count += s.count(t)
# print('Number of vowels: ' + str(count))


# s = 'jkurabcd'
# print(s[4:8])
# result = []
# for i in range(len(s) - 1):
#     smaller = s[i] <= s[i + 1]
#     if smaller:
#         result.append(1)
#     else:
#         result.append(0)
# print(result)
# print(len(result))
# count = 0
# pinnedidx = 0
# maxcount = 0
# for i in range(len(result)):
#     item = result[i]
#     if item == 1:
#         count += 1
#         if i == len(result) - 1 and count > maxcount:
#             maxcount = count
#             pinnedidx = i - maxcount + 1
#     else:
#         if count > maxcount:
#             maxcount = count
#             pinnedidx = i - maxcount
#         count = 0
# print('Longest substring in alphabetical order is: {}'.format(s[pinnedidx:maxcount+ pinnedidx + 1]))


"""
   lect03
"""


# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every
#     # character, including spaces and commas!
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# x = 23
# epsilon = 0.01
# step = 0.1
# guess_number = 0.0
# num_guess = 0
#
# while abs(guess_number**2-x) >= epsilon:
#     if guess_number <= x:
#         guess_number += step
#         num_guess += 1
#     else:
#         break
#
# if abs(guess_number**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess_number))
# print(num_guess)

# """
#     作者：陈笔
#     09/12/2019
#     功能：利用求中法让机器人猜测你想的0-100之间的数据
# """
# print("请在你的心中想象一个0到100之间的数字")
# hi = 100
# lo = 0
# guessed = False
# # 一下进行猜测循环
# while not guessed:
#     guess_number = (hi + lo)//2
#     print("你心中想象的数字是：{}?".format(guess_number))
#     user_inp = input("如果显示的数据比你大，请输入h；"
#                      "如果现实的数据比你小，请输入l；"
#                      "如果显示的数据和你一样，请输入c！")
#     if user_inp == 'c':
#         guessed = True
#     elif user_inp == 'h':
#         hi = guess_number
#     elif user_inp == 'l':
#         lo = guess_number
#     else:
#         print("对不起，您输入的不正确")
#
# print('游戏结束，你心中想的数字是：{}'.format(guess_number))


# # -*- coding: utf-8 -*-
# """
#     作者：陈笔
#     10/12/2019
#     功能：利用牛顿迭代法（Newton-Raphson method），计算数据的平方根
# """
#
# epsilon = 0.01
# y = 54.0
# guess_number = y/2.0
# numGuesses = 0
#
# while abs(guess_number*guess_number - y) >= epsilon:
#     numGuesses += 1
#     guess_number = guess_number - (((guess_number**2) - y)/(2*guess_number))
# print('numGuesses = {}'.format(numGuesses))
# print('Square root of {} is about {}'.format(y , guess_number))

# x = 12
# def g(x):
#       x = x + 1
#       def h(y):
#           return x + y
#       return h(6)
# print(g(x))



"""
   lect 04
"""

# def foo(x, y=5):
#     return bar(y * 2)
# def bar(x):
#     return x + 1
#
# print(foo(3))


# def foo(x, y=5):
#     def bar(x):
#         return x + 1
#
#     return bar(y * 2)
#
#
# print(foo(3,0))


# def foo (x):
#    def bar (z, x = 0):
#       return z + x
#    return bar(3, x)
#
# print(foo(2))


# base = 5
# exp =2
#
# result = 1
# for i in range(exp):
#    result *= base
#
# return result
#
# print(result)


# def recurPower(base, exp):
#    '''
#    base: int or float.
#    exp: int >= 0
#
#    returns: int or float, base^exp
#    '''
#    # Base case is when exp = 0
#    if exp <= 0:
#       return 1
#
#    # Otherwise, exp must be > 0, so return
#    #  base* base^(exp-1). This is the recursive case.
#    return base * recurPower(base, exp - 1)
#
# print(recurPower(4,5))





# """
#    递归法求最大公约数
# """
# def gcdIter(a, b):
#    """该函数返回两个数的最大公约数"""
#
   # 获取最小值
   # if a > b:
   #    smaller = b
   # else:
   #    smaller = a
   #
   # for i in range(1, smaller + 1):
   #    if ((a % i == 0) and (b % i == 0)):
   #       gcdIter = i
   #
   # return gcdIter
#
#
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print(num1, "和", num2, "的最大公约数为", gcdIter(num1, num2))


# """
#    跌代法求最大公约数
# """
# def gcdIter(a, b):
#    r = 1
#    while r != 0:
#       r = a % b  # a比b小则保留a的值；a比b大则保留它们的余数
#       a = b  # b的值赋给a
#       b = r  # r的值赋给b
#
#    return a
#
# print(gcdIter(5, 10))


# def gcdRecur(a, b):
#    '''
#    a, b: positive integers
#
#    returns: a positive integer, the greatest common divisor of a & b.
#    '''
#
#    if a > b:
#       a, b = b, a
#    if b % a == 0:
#       return a
#    else:
#
#       return gcdRecur(a, b % a)
#
# print(gcdRecur(221, 7))




#
# """
#    字符串判断
# """
# def isIn(char, aStr):
#    '''
#    char: a single character
#    aStr: an alphabetized string
#
#    returns: True if char is in aStr; False otherwise
#    '''
#    # Base case: If aStr is empty, we did not find the char.
#    if aStr == '':
#       return False
#
#    # Base case: if aStr is of length 1, just see if the chars are equal
#    if len(aStr) == 1:
#       return aStr == char
#
#    # Base case: See if the character in the middle of aStr equals the
#    #   test character
#    midIndex = len(aStr) // 2
#    midChar = aStr[midIndex]
#    if char == midChar:
#       # We found the character!
#       return True
#
#    # Recursive case: If the test character is smaller than the middle
#    #  character, recursively search on the first half of aStr
#    elif char < midChar:
#       return isIn(char, aStr[:midIndex])
#
#    # Otherwise the test character is larger than the middle character,
#    #  so recursively search on the last half of aStr
#    else:
#       return isIn(char, aStr[midIndex + 1:])


import math

def polysum(n, s):

   area = (0.25 * n * s**2) / math.tan(math.pi / n)
   # print('%.4f' %area)
   perimeter = n * s
   sum_of_area_and_sqperi = area + perimeter ** 2

   return float('%.4f' % sum_of_area_and_sqperi)

print(polysum(19, 65))


