def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fib_iterative(n):
    if n<=1:
        return n
    prev = 0
    current = 1
    for _ in range (2, n+1):
        next = current + prev
        prev, current = current, next
    return current
print(fibonacci(5))