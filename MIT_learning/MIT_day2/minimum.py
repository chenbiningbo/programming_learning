def minimum(a, b):
    if a >b:
        return print('the minimum num is', b)
    elif a <b:
        return print('the minimum num is', a)
    else:
        print('equal')


a = float(input('please input numa:'))
b = float(input('please input numb:'))

minimum(a, b)