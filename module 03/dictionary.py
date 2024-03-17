# key value pair
# dictionary
# object
# hash table
# overlap with set

persion = {'name': 'kala pakhi', 'address': 'kaliapur', 'age': 23, 'job': 'facebooker'}
print(persion)
print(persion['job'])
print(persion['age'])
print(persion.keys())
print(persion.values())
persion['language'] = 'python'
persion['name'] = 'sada pakhi'
print(persion)

# special dictionary looping
for key, value in persion.items():
    print(key, value)