"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

print("You can +, -, *, **, / and %. 'q' to quit")

inputs_lst = ["+", "-", "*", "**", "/", "%"]

while True:
    calculation = input("select action, num1 and num2 >")
    inputs = calculation.split(" ")
    operand = inputs[0]

    if operand == 'q':
            break

    elif len(inputs) < 3 or len(inputs) > 3 or not inputs[1].isdigit() or not inputs[2].isdigit():
        print("Invalid input, ex. + 1 2. Try again!")

    else:
        num1 = float(inputs[1])
        num2 = float(inputs[2])
        
        if operand not in inputs_lst:
            print("Invalid, try again")

        elif operand == "+":
            result = add(num1, num2)

        elif operand == "-":
            result = subtract(num1, num2)

        elif operand == "*":
            result = multiply(num1, num2)

        elif operand == "**":
            result = power(num1, num2)

        elif operand == "/":
            result = divide(num1, num2)

        elif operand == "%":
            result = mod(num1, num2)

        print(result)