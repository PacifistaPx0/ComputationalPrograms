import math

def f(x):
    return x**4 + x -3

def df(x):
    return 4 * x**3 + 1

def Newton_Rhap(f, df, n=0, iter=100):
    """
    Implementation of the Newton-Raphson method for finding the root of a function f.
    :param f: the function whose root is to be found
    :param df: the derivative of f
    Using the lower bound as the initial guess
    """

    #Finding the closed interval of the root
    while n>=0:
        if f(n) * f(n+1) > 0:
            n +=1
        break
    x=n
    for i in range(iter):
        x = x - f(x)/df(x)
    return x

root = Newton_Rhap(f, df)

print(f"The root of the equatuion  (x**4+x-3) is: {root:.15f}")
