def add(x: float, y: float) -> float:
    """Adds two numbers together."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtracts the second number from the first."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiplies two numbers together."""
    return x * y

def divide(x: float, y: float) -> float:
    """Divides the first number by the second. Raises ValueError if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x: float, y: float) -> float:
    """Raises the first number to the power of the second."""
    return x ** y

def mod(x: float, y: float) -> float:
    """Returns the remainder of the division of the first number by the second."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x % y

if __name__ == '__main__':
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 3))
    print("Power:", power(5, 3))
    print("Modulus:", mod(5, 3))

