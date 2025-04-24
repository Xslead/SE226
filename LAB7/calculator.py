import math_utils

operator_dict = {
    "add" : math_utils.add,
    "subtract" : math_utils.subtract,
    "multiply" : math_utils.multiply,
    "divide" : math_utils.divide,
    "power" : math_utils.power,
    "mod" : math_utils.mod
}

def main():
    print("Welcome to the calculator!")
    print("Available operations: add, subtract, multiply, divide, power, mod")
    operation = input("Please enter the operation you want to perform: ")

    if operation not in operator_dict:
        print("Invalid operation. Please try again.")
        return

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    result = operator_dict[operation](x, y)
    print(f"The result of {operation}({x}, {y}) is: {result}")

if __name__ == "__main__":
    main()
