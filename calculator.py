#Create a simple calculator program using python


#using +,-,*,/
#allow user enter first number ,operator,second number ,and gives result based on entered operator


# Simple Calculator

# input from user
x = float(input("Enter first number: "))
operator = input("Enter sign (+, -, *, /): ")
y = float(input("Enter other number: "))

# calculation
if operator == "-":
    result = x - y
elif operator == "+":
    result = x + y
elif operator == "/":
    if y != 0:
        result = x / y
    else:
        result = "Error! A number cannot be divided by 0"
elif operator == "*":
    result = x * y

else:
    result = "Unaccepted "

# output
print("Result:", result)


























