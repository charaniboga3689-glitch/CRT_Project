'''for and while 
Syntax:
for  variable in iterable:
    # code block to be executed
n = int(input("Enter a num: "))
for i in range(1, n+1):
    print(i)    
'''
n = int(input("Enter a num: "))
for i in range(1, n+1):
    print(i,end=" ")
i = 1
while i <= n:
    print(i)
    i += 1
name = "Boga Charani"
i = 0
while i <= 5:
    print(name)
    i += 1        
name = "Boga Charani"
for i in range(len(name)):
    print("Index:", i, "Character:", name(i))    

marks = 45
if marks >= 40:
    print("Pass")
else:
    print("Fail")    