#Create a simple calculator program using python


#using +,-,*,/
#allow user enter first number ,operator,second number ,and gives result based on entered operator


# Simple Calculator

# input from user
num1 = float(input("Enter first number: "))
operator = input("Enter sign (+, -, *, /): ")
num2 = float(input("Enter other number: "))

# calculation
if operator == "-":
    result = num1 - num2
elif operator == "+":
    result = num1 + num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! A number cannot be divided by 0"
elif operator == "*":
    result = num1 * num2

else:
    result = "Unaccepted "

# output
print("Result:", result)


























