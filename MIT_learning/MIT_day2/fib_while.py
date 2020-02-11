F1, F2 = 0, 1
count = 2
nterms = 13
print(F1)
print(F2)
while count < nterms:
    Fn = F1 + F2
    print(Fn)
    F1 = F2
    F2 = Fn
    count += 1