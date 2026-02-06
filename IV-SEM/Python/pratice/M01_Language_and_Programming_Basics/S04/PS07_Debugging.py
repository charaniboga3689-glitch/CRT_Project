'''
Docstring for IV-SEM.Python.pratice.M01_Language_and_Programming_Basics.S04.PS07_Debugging
Debugging in python:
bug--> errors in the program
Debugging --> Finding and Fixing of errors

TYPES OF ERRORS:
1. Syntax Erroes--> Missing of colon, missing of indentation
2. Runtime Errors--> Division by zero, file not found 
3. Logical Errors--> Missing of logic

Debugging Techniques:
1. Print statements debugging
2. try-except
3. using pdb
  pdp--> Python Debugger
  purpose:
  1. Pause the execution code
  2. Inspect the variables's value
  3. To run the code line by line
  pdp Commands:
  1. n--> To execute the output in a next line
  2. p--> to get the value of a variable
  3. l--> list nearby  code
  4. c--> coontinue the execution
  5. r--> return from thr function
  6. s--> to start a function
  7. h--> help
  8. q--> quit the execution

try:
    a= int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("can not divsible by zero.")
except ValueError:
    print("Invalid input")           
'''
import pdb

def add(a, b):
    pdb.set_trace() # Set a breakpoint here
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(a,b))