# string is a sequence of characters
name = 'Sakib\'s khan' #escape
name2 = "Sakib khan"
# multiline string
name3 = """ 
    Sakib khan
    number one
 """
print(name3)

for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])

# mutable means changeable 
# immutable means you can not change it
print(name2)
if 'khan' in name2:
    print('exists')

print(name2.upper())