fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'egg', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print(first_three)
print(last_three)
