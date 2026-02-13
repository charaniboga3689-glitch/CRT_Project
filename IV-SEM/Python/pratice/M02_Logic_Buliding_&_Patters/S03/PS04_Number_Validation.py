'''
1. Armstrong number 
n = int(input())
l = len(str(n))
res = 0
for i in str(n):
    res += int(i) ** l
print("Armstrong" if n == res else "not Armstrong")    

2. Perfect number
n = 6
1 + 2 + 3 = 6

code:
n = int(input())
s = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        s += i
print("perfect" if n == s else "not perfect")   

3. Strong number

def factorial(n):
    if n < 0:
        return "no factorial for -ve"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= 1
        return fact
s = 0
n = int(input())
for i in str(n):
    s += factorial(int(i))

print("strong number" if n == 5 else "not strong number")        
'''
