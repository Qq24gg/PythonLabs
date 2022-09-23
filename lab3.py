a = int(input())
b = int(input())
c = int(input())
if (b and c) < a:
    print(a, 'наибольшее')
elif (a and c) < b:
    print(b, 'наибольшее')
else:
    print(c, 'наибольшее')
    
