import math

def func(x):
    return x * math.exp(x) - 1

def bisection(func, a, b, tol):
    """
    Finds a root of the function 'func' in the interval [a, b]
    using the bisection method, with a stopping criterion of
    'tol' percent relative error.
    """
    if func(a) * func(b) > 0:
        raise ValueError("function must have opposite signs at end points")
    c=(a+b)/2
    fc=func(c)
    while b-a>tol:
        fa=func(a)
        fb=func(b)
        if fc>0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc
        c=(a+b)/2
        fc=func(c)
    return c

a=0
b=1
tol=0.05

root = bisection(func, a, b, tol)
print(f"The root of the equatuion is: {root:.5f}")
