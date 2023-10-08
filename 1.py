print("Введите строку символов латинского алфавита")
s = input()
xd = list(s)
xdd = ''
k = 0
le = ' '

for i in range(len(xd)):
    k = 0

    if xd[i] == le:
        continue

    else:
        for j in range(i, len(xd)):

            if xd[i] == xd[j]:
                k = k + 1
                le = xd[i]

            else:
                break

        xdd = xdd + xd[i]

        if k > 1:
            xdd = xdd + repr(k)

print(xdd)
