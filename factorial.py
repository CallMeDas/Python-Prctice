a=6
def fact(n):
    if n < 0:
     return "Factorial is not defined for negative numbers."
    elif n == 0:
     return 1
    else:
      result = 1
    for i in range(1, n + 1):
      result *= i
    return result

factorial=fact(a)
print(f"The factorial of {a} is", factorial)