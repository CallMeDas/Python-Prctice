a = input("Enter first number: ")
b = input("Enter second number: ")


try:
  a = int(a)
  b = int(b)
except ValueError:
  print("Invalid input. Please enter numbers only.")
  exit() 


sum = a + b

print(f"The sum of {a} and {b} is: {sum}")

