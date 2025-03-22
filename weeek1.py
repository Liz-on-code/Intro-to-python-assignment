

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

mathematical_operation = input("Enter an operation (+, -, *, /): ") 

if mathematical_operation == "+":
    result = num1 + num2 
    print(f"{num1} + {num2} = {result}")

elif mathematical_operation == "-":
    result = num1 - num2 
    print(f"{num1} - {num2} = {result}")

elif mathematical_operation == "*":
    result = num1 * num2 
    print(f"{num1} * {num2} = {result}")

elif mathematical_operation == "/":
    result = num1 / num2 
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation")



