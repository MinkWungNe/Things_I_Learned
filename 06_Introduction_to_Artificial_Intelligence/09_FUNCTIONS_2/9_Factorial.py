def factorial(n):
    if n > 1:
        return factorial(n-1) * n
    else:
        return 1
    
# TEST 
result = factorial(5)
print(result)