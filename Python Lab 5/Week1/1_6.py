ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

average_age = sum(ages) / len(ages)
min_age = min(ages)
max_age = max(ages)

min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)

print(min_average_diff)
print(max_average_diff)
