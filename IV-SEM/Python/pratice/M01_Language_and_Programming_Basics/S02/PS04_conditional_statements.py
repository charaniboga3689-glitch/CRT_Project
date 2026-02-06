#Read a number from the user and check if is +ve, -ve or zero

'''
Input = 10
output = '+ve'

Input = 0
output = 'zero

Intput = -5
output = '-ve
'''

n = int(input())
if n > 0:
    print("+ve")
elif n == 0:
    print("zero")
else:
    print("-ve")     