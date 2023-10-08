def symbols(inp):
    d = {}
    for element in inp:
        if d.get(element, None):
            d[element] += 1
        else:
            d[element] = 1

    return d

print("Введите строку символов латинского алфавита")
s = input()
xd = list(s)

print(symbols(xd))
stt = sorted(symbols(xd).items(), key=lambda item: item[1], reverse=True)

for i in range(0, 3):
    print(stt[i])


