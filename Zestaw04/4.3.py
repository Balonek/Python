def factorial(n):
    result = 1
    for x in range(1,n+1):
        result *= x
    return result

assert factorial(5) == 120
assert factorial(0) == 1  
assert factorial(1) == 1  
assert factorial(2) == 2
