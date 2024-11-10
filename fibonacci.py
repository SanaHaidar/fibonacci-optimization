# Basic Recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Memoization
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Bottom-Up Approach
def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# Test_Cases


def test_fibonacci():
    assert fibonacci_recursive(10) == 55
    assert fibonacci_memo(10) == 55
    assert fibonacci_bottom_up(10) == 55
    print("All tests passed.")


if __name__ == "__main__":
    test_fibonacci()
