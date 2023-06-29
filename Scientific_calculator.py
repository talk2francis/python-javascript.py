import math

def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers."""
  return x / y

def power(x, y):
  """Raises a number to a power."""
  return x ** y

def square_root(x):
  """Returns the square root of a number."""
  return math.sqrt(x)

def factorial(x):
  """Returns the factorial of a number."""
  if x == 0:
    return 1
  else:
    return x * factorial(x - 1)

def main():
  """Prints the results of some mathematical operations."""
  print(add(1, 2))
  print(subtract(10, 5))
  print(multiply(2, 3))
  print(divide(10, 2))
  print(power(2, 3))
  print(square_root(16))
  print(factorial(5))

if __name__ == "__main__":
  main()
