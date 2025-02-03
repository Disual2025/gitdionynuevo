frutas = {"orange", "strawberry", "apple"," lemon"}
print(frutas)
print(len(frutas))
set1 = {"apple", "banana", "cherry","mango"}
set2 = {1, 5, 7, 9, 3,"banana"}
set3 = {True, False, False}
print(set2)
print(set1)
print(set3)
print(len(set3))
set4 = set1.union(set3)
print(set4)
print(len(set4))
set5 = set1.union(set2)
print(set5)
set6 = set1.intersection(set2)
print(set6)