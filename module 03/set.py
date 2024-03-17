# list  --> []
# tuple --> ()
# set   --> {}
# set: unique items collection. no duplicate
numbers = [12, 56, 98, 78, 56, 12, 6, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)