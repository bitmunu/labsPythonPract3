print("Введите строку символов латинского алфавита")
s = input()
xd = list(s)
xdd = ''
k = 0
number = ''
cur = 0


def isdigit(a):
    digits = "123456789"
    digits = list(digits)

    y = 0
    for digit in digits:
        if a == digit:
            y = 1
            break

    if y == 1:
        return 1
    else:
        return 0


for i in range(len(xd)):
    number = ''
    if isdigit(xd[i]) == 0:
        cur = xd[i]
        xdd += cur

    else:
        number += xd[i]

        for j in range(i + 1, len(xd)):
            if isdigit(xd[j]):
                number += xd[j]
            else:
                break
        xdd += cur * (int(number) - 1)

print(xdd)