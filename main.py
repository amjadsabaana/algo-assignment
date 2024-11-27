import time

# itterative
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# اthe number we insert 
number = 100;

# itterative method 
#start_iterative = time.time()
#iterative_result = factorial_iterative(number)
#end_iterative = time.time()
##print(f"Factorial (Iterative): {iterative_result}")
#print(f"Time taken (Iterative): {(end_iterative - start_iterative) * 1000:.5f} milliseconds")

# recursive method 
start_recursive = time.time()
recursive_result = factorial_recursive(number)
end_recursive = time.time()
print(f"Factorial (Recursive): {recursive_result}")
print(f"Time taken (Recursive): {(end_recursive - start_recursive) * 1000:.5f} milliseconds")
