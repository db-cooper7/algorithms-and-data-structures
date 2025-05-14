import sys

# read notes about recursion written in **factorial.py**

# Recursive implementation to calculate the n-th Fibonacci number
def fibonacci(n: int):
    # Base case: n = 0 || n = 1
    if n <= 1:
        return n
    
    # Recursive case: fibonacci(n): fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n - 1) + fibonacci(n - 2)


r"""
nodes:                                                     level:
1                       fib(5)                              0
                          /\
                         /  \
                        /    \
                       /      \
2                   fib(4) +  fib(3)                        1
                    /\           /\
                   /  \         /  \
                  /    \       /    \
                 /      \     /      \
4               fib(3) + fib(2)   fib(1)                    2
                         / \
                        /   \
                       /     \
                      /       \
8               fib(1)      +  fib(0)                       3
"""

# Time complexity: O(2^n) -> each node itself is a function call and simply calculates
# the sum of two values, and each of these two values calls upon itself again
# Space complexity: O(n) -> call stack grows linearly with n
# https://stackoverflow.com/questions/28756045/what-is-the-space-complexity-of-a-recursive-fibonacci-algorithm

def main():
    if len(sys.argv) < 2:
        print("usage: fibonacci.py <positive number>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("must be a positive number")
    except ValueError as e:
        print(f"something went wrong: {e}")
        sys.exit(1)
    print(f"fib({n}) = {fibonacci(n)}")

if __name__ == "__main__":
    main()
