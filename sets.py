#set is a collection of data which is unordered, unindexed and No duplicates


utensils = {"fork", "knives", "glasses"}
dishes = {"bowl", "plate", "cup", "knives", "spoons"}


utensils.add("spoons")

dishes.remove("knives")

#print(utensils, dishes)

#utensils.update(dishes)

#print(utensils)

utensils.intersection(dishes)

print(utensils)