import time

res = [0, 1, 1]


def fib2(n: int) -> int:
    if n < 0:
        return - 1
    if n <= 2:
        return res[n]
    if n < len(res):
        return res[n]
    res.append(fib(n - 2) + fib(n - 1))
    return res[-1]


def fib(n: int) -> int:
    if n < 0:
        return - 1
    if n <= 2:
        return res[n]
    return fib(n-1)+fib(n-2)


if __name__ == "__main__":
    u1 = time.time()
    print(fib2(20))
    u2 = time.time()
    print(str(u2 - u1) + 's')
