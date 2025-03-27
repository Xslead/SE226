from locale import currency


def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

var = lambda x, k, n: (-1) ** n * x ** k / factorial(k)

def sine_x(x,n):
    """
    Recursively calculates the sine of x using the first n terms of the Taylor series.
    :param x: Real number
    :param n: Non-negative integer
    :return: Infinite loop for the sum of the first n terms of the Taylor series
    """
    curr_sum = 0
    for i in range(n + 1):
        k = 2 * i + 1
        curr_sum += var(x,k,i)

    return curr_sum

harmonic_sum = 0
def harmonic_number(n):
    """
    Recursively calculate the nth Harmonic number using a global variable.
    Computes Hn = 1 + 1/2 + 1/3 + ... + 1/n by updating the global 'harmonic_sum'.
     n: Positive integer defining the Harmonic series limit
     effect: Modifies global 'harmonic_sum'
    :complexity: O(n) time and space
    """
    global harmonic_sum
    if n <= 0:
        return

    if n == 1:
        harmonic_sum = 1
        return

    harmonic_number(n - 1)

    harmonic_sum += 1 / n
