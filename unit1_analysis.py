from unit1_recursion import *
print("factorial:")
print(f"factorial of {0} is {factorial(0)}")
print(f"factorial of {5} is {factorial(5)}")


print("\nFibonacci:")
print(fib_naive(0))
print(fib_naive(1))
print(fib_naive(10))

print("\nHanoi:")
hanoi(3, 'A', 'B', 'C')

print("\nBinary Search:")
a = [1,3,5,7,9,11]
print(binary_search_rec(a, 7, 0, len(a)-1))
print(binary_search_rec(a, 2, 0, len(a)-1))