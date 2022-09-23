a = int(input())
b = int(input())
c = int(input())

if (a == b or a == c or b == c) and not (a == b and b == c):
    print('2')
elif a == b and b == c:
    print('1')
else:
    print('3')
