# 1, 1, 2, 3, 5, 8
#to compute fibonacci number of an integer n
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2)+fib(n-1)

print(fib(6))