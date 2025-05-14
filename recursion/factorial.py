import sys

"""
    Recursion, simply put is when a function calls it self, blowing up the call stack after many
    function calls, using the whole memory available

    Its usually possible to convert a recursive solution into an iterative one, and vice versa

    Recursive functions are broken down into two parts:

    1- The base case;
    2- The recursive case.

    If we want to compute the n! (factorial), we can use recursion. The foruma is as follows:

    n! = n * (n - 1) * (n - 2)! 

    For instance, to compute 5!, we could break drown into 5 * 4!, and 4! can be broken down into 4 * 3!
    and so on...
    The base case is when n = 0 or n = 1. Both results yield 1 
"""

# Recursive implementation of n! (n-factorial) calculation, assuming n to be an element of N, including 0:
def recursive_factorial(n: int):
    # Base case:
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * recursive_factorial(n-1)

# Time complexity: O(n) -> only n calls are being made to the factorial function, each function call is O(1)
# Space complexity: O(n) -> although not using any data structure, recursion operates off of an implicit stack
# that is how we're able to return from one function call to the other, sort of a chain of function calls

def iterative_factorial(n: int):
    if n <= 1:
        return 1
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res

def main():
    if len(sys.argv) < 3:
        print("usage: python3 factorial.py <number> <mode: i(iterative)|r(recursive)>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("number must be non-negative")
    except ValueError as e:
        print(f"invalid number: {e}")
        sys.exit(1)
    
    mode = sys.argv[2].lower()
    if mode == 'r':
        res = recursive_factorial(n)
    elif mode == 'i':
        res =  iterative_factorial(n)
    else:
        print("invalid mode")
        sys.exit(1)
    
    print(f"{n}! ({mode}) = {res}")

if __name__ == "__main__":
    main()