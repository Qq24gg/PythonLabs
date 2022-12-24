numbers = [54, 32, 23, 75, 5, 23, 76, 30, 95, 10]
 
a = 0
 
for i in numbers:
    a += i
 
print(a)



a = 0
numbers = [0, 8, 2, 8, 0, 3, 0, 2, 69, 0, 46, 90, 0]
for i in numbers:
    if i == 0:
        a += 1
print(a)



n = int(input())
for i in range(1, n+1):
    print(" "*(i-1)+""+ str(i))



n = int(input()) + 1
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print(*range(1, i), *range(1, i - 1)[::-1], sep='')