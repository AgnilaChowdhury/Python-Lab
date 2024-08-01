def geometric_sequence(a, r, n):
    for i in range(n):
        term = a * (r ** i)
        print(f"Term {i+1}: {term}")

a = 2  # first term
r = 3  # common ratio
n = 6  # number of terms

print("Geometric sequence:")
geometric_sequence(a, r, n)