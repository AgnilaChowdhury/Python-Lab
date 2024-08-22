A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

del A
del B

try:
    print("A:", A)
except NameError:
    print("A has been deleted.")

try:
    print("B:", B)
except NameError:
    print("B has been deleted.")
