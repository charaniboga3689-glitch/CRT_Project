'''
1.Writ a python code to count the digits of number?
ex: 15678--> output: 5
n = int(input())
count = 0 
while n > 0:
    count += 1 
    n //= 10  
print("Number of digits:", count)

2.sum of the digits of a number?
ex:12345-->1+2+3+4+5=15
n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    n //= 10
print("Sum of digits:", sum_digits)

3. Product of digits of a number?
n = int(input("Enter a number: "))
product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n //= 10

print("Product of digits:", product)

4. Reverse of a number?
n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number:", reverse)

5. Count the even and odd digits?
n = int(input("Enter a number: "))
even_count = 0
odd_count = 0

n = abs(n)

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)

6. print the largest digit of a number?
n = int(input("Enter a number: "))
largest = 0

n = abs(n)

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10

print("Largest digit:", largest)
'''


