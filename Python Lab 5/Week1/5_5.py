A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

join_ab = A.union(B)
join_ba = B.union(A)

print("Join A with B:", join_ab)
print("Join B with A:", join_ba)
