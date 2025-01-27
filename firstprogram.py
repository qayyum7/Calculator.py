def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
def square_root(a):
    if a < 0:
        return "Error: Square root of a negative number is not defined!"
    return math.sqrt(a)
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. square root")

choice = int(input("Enter your choice (1-5): "))
num1 = float(input("Enter first number: "))

if choice in [1, 2, 3, 4]:
    num2 = float(input("Enter second number: "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = sub(num1, num2)
elif choice == 3:
    result = mul(num1, num2)
elif choice == 4:
    result = div(num1, num2)
elif choice == 5:
    result = square_root(num1)
else:
    result = "Error: Invalid choice!"

print("Result:", result)