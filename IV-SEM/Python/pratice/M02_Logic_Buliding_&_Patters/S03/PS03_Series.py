'''
1.Display Arithmetic Progression values upto 10
a = int(input())
d = int(input())
for i in range(10):
    print(a + (i*d),end= " ")

2. Fibonacci series upto 10 terms    
a = 0
b = 1
n = int(input())
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

list = [0,1]
for i in range(2, n):
    list[i - 2] + list[i - 1]
print(list)    

3. Power Series
#input : 2
#output : 2, 4, 8, 16
n = int(input())
for i in range(1, 11):
    print(n ** i, end=" ")
'''
