c = [[('e', []), 'g','h'], ['a','b','c']]

for i, x in enumerate(c):
    for j, y in enumerate(c[i]):
        if 'e' == y[0]:
            for k, z in enumerate(x[j][1]):
                if 'huy' == z[0]:
                    print('hello')
                    break
            x[j][1].append('huy')
            break

print(c)