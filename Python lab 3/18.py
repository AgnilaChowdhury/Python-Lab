def generate_combinations():
    values = [1, 2, 3]

    for i in values:
        for j in values:
            for k in values:
                print(i, j, k)

generate_combinations()
