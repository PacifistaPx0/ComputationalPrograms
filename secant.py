def f(x):
    # Define the function whose root we want to find
    return x**2 - 3*x + 2

def secant_method(f, x0, x1, tol, maxiter):
    # Implement the secant method
    i = 0
    while abs(f(x1)) > tol and i < maxiter:
        x_next = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x_next
        i += 1
    if i == maxiter:
        print("Maximum iterations exceeded.")
    else:
        print("The root is approximately:", x1)

# Example usage
secant_method(f, 0, 2, 1e-6, 100)
