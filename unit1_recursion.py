#""""FACTORIAL FUNCTION""""
def factorial(num):
    if num==0 or num==1:            #Base Case 
        return 1
    return num*factorial(num-1)      #Recursive case

#"""FIBONNACI FUNCTION"""
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

#"""HONAI """
def hanoi(n, src, aux, dst):
    if n == 1:
        print(f"Move disk 1 from {src} to {dst}")
        return
    hanoi(n-1, src, dst, aux)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n-1, aux, src, dst)

#"""BINARY SEARCH """
def binary_search_rec(a, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == target:
        return mid
    elif target < a[mid]:
        return binary_search_rec(a, target, lo, mid-1)
    else:
        return binary_search_rec(a, target, mid+1, hi)