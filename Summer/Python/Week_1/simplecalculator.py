# Simple Calculator Program

# Get first number from user
num1 = float(input("Enter the first number: "))

# Get operator from user
operator = input("Enter an operator (+, -, *, /, %): ")

# Get second number from user
num2 = float(input("Enter the second number: "))

# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    # Avoid division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
elif operator == "%":
    # Avoid modulo by zero
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error: Cannot perform modulo with zero"
else:
    result = "Invalid operator"

# Show the result
print("Result:", result)
