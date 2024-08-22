fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'egg', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

n = len(food_stuff_lt)
if n % 2 == 0:
    middle_items = food_stuff_lt[n//2 - 1:n//2 + 1]
else:
    middle_items = [food_stuff_lt[n//2]]

print(middle_items)
