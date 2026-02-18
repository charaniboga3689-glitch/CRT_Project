'''
1. Read a number from the user and count the factors.
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i, end=" ")
print(count)

2. Reverse Integer (leet code)
n = int(input())
if n >= 0:
    print(int(str(n)[::-1]))
else:
    n = -1 * n
    print(-1 * int(str(n)[::-1]))    

    (or)
n = int(input())
if n < 0:
     n = -1 * n
     print(-1 * int(str(n)[::-1]))    

3. Plus One(leet code)

Logic: Convert the number to a list of digits, add one to the last digit, and handle anny carry that may occur.

'''
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0   
        
        return [1] + digits

