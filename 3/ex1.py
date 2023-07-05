a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 1 вариант
# for i in a:
#     if i < 5:
#         print(i)


# 2 вариант который лучше
num = int(input('Введте цифру'))
for i in a:
    if i < num:
        print(i)
