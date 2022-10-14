from itertools import *

symbols = 'NESODRMY'
numbers = [0,1,2,5,6,7,8,9]
v = []

for i in range(0, len(symbols)):
    a = []
    a.append(symbols[i])
    a.append(0)
    v.append(a)

for i in permutations(numbers, len(numbers)):
    for j in range(0, 8):
        v[j][1] = i[j]
    send = str(v[2][1]) + str(v[1][1]) + str(v[0][1]) + str(v[4][1])
    more = str(v[6][1]) + str(v[3][1]) + str(v[5][1]) + str(v[1][1])
    money = str(v[6][1]) + str(v[3][1]) + str(v[0][1]) + str(v[1][1]) + str(v[7][1])
    send, more, money = int(send), int(more), int(money)

    if send + more == money:
        print('\n\n\n\nENCONTRO:')
        print('SEND:', send)
        print('MORE', more)
        print('MONEY', money)
        break

    print('SEND:', send)
    print('MORE', more)
    print('MONEY', money)