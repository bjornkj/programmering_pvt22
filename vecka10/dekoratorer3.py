import time
import functools

# Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144


# En primitiv implementation av memoize
def memoize(f):
    mem = {}
    def inner(*args):
        if args in mem:
            return mem[args]
        result = f(*args)
        mem[args] = result
        return result
    return inner


@functools.cache
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)



if __name__ == '__main__':
    start_tid = time.time()
    print(fibonacci(40))
    print(f"tog {time.time() - start_tid} sekunder")



#                           fibonacci(3)
#                             /    \
#                  fibonacci(2)   fibonacci(1)
#                  /      \             \
#         fibonacci(1)   fibonacci(0)    fibonacci(0)
