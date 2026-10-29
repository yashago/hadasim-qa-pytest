"""Simple calculator functions."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    return base ** exponent


def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot take modulo by zero")
    return a % b

print(0.1)
print(0.2)
print(0.1 + 0.2)