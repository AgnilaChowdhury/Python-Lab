import cmath

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return (-c / b,)

    discriminant = b**2 - 4*a*c
    sqrt_discriminant = cmath.sqrt(discriminant)

    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return (x1, x2)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
solutions = solve_quadratic_eqn(a, b, c)
print(solutions)  # Output should be ((2+0j), (1+0j))
