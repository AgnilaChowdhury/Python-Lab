import math

# a) sin of 60 degree
# Note: math.sin() function takes input in radians, so we need to convert 60 degrees to radians
result_a = math.sin(math.radians(60))
print(f"Sin of 60 degree is: {result_a}")

# b) cos of pi
result_b = math.cos(math.pi)
print(f"Cos of pi is: {result_b}")

# c) sin(0.8660254037844386)
# Note: This value is actually the sin of 60 degrees, so we expect the result to be the same as (a)
result_c = math.sin(0.8660254037844386)
print(f"Sin(0.8660254037844386) is: {result_c}")

# d) tan of 90 degree
# Note: tan(90 degrees) is undefined in mathematics, so we expect a large value or an error
result_d = math.tan(math.radians(90))
print(f"Tan of 90 degree is: {result_d}")