def is_eligible(math, physics, chemistry):
    if math >= 60 and physics >= 50 and chemistry >= 40:
        if math + physics + chemistry >= 200 or math + physics >= 150:
            return True
    return False

n = int(input("Enter the number of students: "))

eligible_candidates = []

for i in range(n):
    print("Enter marks for student", i+1, ":")
    math = int(input("Mathematics: "))
    physics = int(input("Physics: "))
    chemistry = int(input("Chemistry: "))

    if is_eligible(math, physics, chemistry):
        eligible_candidates.append(i+1)

if eligible_candidates:
    print("The following candidates are eligible:")
    for candidate in eligible_candidates:
        print("Candidate", candidate)
else:
    print("No candidates are eligible.")