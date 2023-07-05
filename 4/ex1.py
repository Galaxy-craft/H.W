b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 1
c = 0


# while 10:
# for i in b:
#     b[c] = b[c] * a
#     c += 1
# a += 1
# c = 0
#
# print(b)
while a < 11:
    for i in b:
        tmp[c] = b[c] * a
        c += 1
    a += 1
    c = 0
    print(tmp)
