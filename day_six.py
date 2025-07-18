tuple = ()
sisters = ("Alice", "Beth", "Cathy")
brothers = ("David", "Ethan", "Frank")
siblings = sisters + brothers                       
print ("Estos son tus hermanos:",len(siblings))
familia_completa= siblings + ("Mercedes", "Jesus")

#level 2

*all_siblings, father, mother = familia_completa
print("Hermanos:", all_siblings)
print("Padre:", father)
print("Madre:", mother)


fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "lettuce", "tomato")
animal_products = ("milk", "cheese", "egg")


food_stuff_tp = fruits + vegetables + animal_products
print("food_stuff_tp:", food_stuff_tp)
#convirtiendo tuple a lista
food_stuff_lt = list(food_stuff_tp)
print("food_stuff_lt:", food_stuff_lt)


length = len(food_stuff_lt)
if length % 2 == 0:
    middle_items = food_stuff_lt[length//2-1:length//2+1]
else:
    middle_items = [food_stuff_lt[length//2]]
print("Elemento(s) del medio:", middle_items)

#lo primeros tres y ultimos 3
print("Primeros tres:", food_stuff_lt[:3])
print("Últimos tres:", food_stuff_lt[-3:])


del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia es país nórdico?", "Estonia" in nordic_countries)
print("Iceland es país nórdico?", "Iceland" in nordic_countries)

 