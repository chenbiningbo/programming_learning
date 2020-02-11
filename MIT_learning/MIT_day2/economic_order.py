# D = float(input('please input Demand(float):'))
# Ct = float(input('please input Ordering cost(float):'))
# Ce = float(input('please input Holding cost(float):'))
# Q = ((2 * D * Ct)/Ce) ** 0.5
# print('the economic order quantity is ', round(Q, 3))


def eqoq(D, Ct, Ce):
    return ((2 * D * Ct)/Ce) ** 0.5

if __name__ == '__main__':
    D = float(input('please input Demand(float):'))
    Ct = float(input('please input Ordering cost(float):'))
    Ce = float(input('please input Holding cost(float):'))
    print('the economic order quantity is ', round(eqoq(D, Ct, Ce), 3))
