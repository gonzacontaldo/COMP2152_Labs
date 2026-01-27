monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")

print("Monday class students:", monday_class)
print("Wednesday class students:", wednesday_class)

intersection = monday_class & wednesday_class
print("Students in both classes:", intersection)

union = monday_class | wednesday_class
print("All students in either class:", union)

only_monday = monday_class - wednesday_class
print("Students only in Monday class:", only_monday)

only_one_class = monday_class ^ wednesday_class
print("Students in only one class:", only_one_class)

is_monday_subset = monday_class <= union
print("Is Monday class a subset of all students?", is_monday_subset)
