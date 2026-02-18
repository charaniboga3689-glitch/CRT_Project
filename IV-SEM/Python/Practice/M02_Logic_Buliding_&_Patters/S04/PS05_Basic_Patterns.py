'''
1.Input : 4
  output :
    * * * *
    * * * *
    * * * *
    * * * *

n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end= " ")
    print()

2. Input : 4
   output:
    *
    * *
    * * *
    * * * *    

n = int(input())
for i in range(n):
    for j in range(i + 1):
        print("*", end= " ")
    print()    

    (or)

n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print("*", end= " ")
    print()    

3. Input: n = 4
output:
* * * *
* * *
* *
*  

n = int(input())
for i in range(n):
    for j in range(n - i):
        print("*", end= " ")
    print()    

    (or)

n = int(input())
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end= " ")
    print()    

    (or)

n = int(input())
for i in range(n):
    for j in range(n - i, 0, -1):
        print("*", end= " ")
    print()  

4. input: n = 4
output: 
1
2 3
4 5 6
7 8 9 

n = int(input())
nums = 1
for i in range(n):
    for j in range(i + 1):
        print(nums, end= " ")
        nums += 1
    print()   

    (or)

k = 1
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(k, end= " ")
        k += 1
    print() 

5. input: n = 4
output:
A   
A B
A B C
A B C D

print(ord('A')) 
print(chr(65))

n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end= " ")
    print()     

6.input: n  = 4
output:

A
B C
D E F
G H I J

n = int(input())
k = 0
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + k), end= " ")
        k += 1
    print()    

    (or)

n = int(input())
k = 0
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + k), end= " ")
        k += 1
    print()  

print("-----------------------------")
n = int(input())      
k = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(k), end= " ")
        k += 1
    print()    

7. Hollow square pattern
input: n = 4
output:
* * * *
*     *
*     *
* * * *

n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()            

'''
