n = int(input('Enter a number: '))
print(list(range(1,n+1)))

from math import sqrt


for x in range(2, n):
    if not any(y for y in range(2, 1+int(sqrt(x))) if not x % y):
        print(x)

