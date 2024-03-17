""" def full_name(first, last):
    name = f'Full name is: {first} {last}'
    return name
# take parameters in order (serial wise)
# name = full_name("NAHID", "HASAN")
# take parameters in unorder
name = full_name(last="HASAN", first="NAHID")
print(name) """

# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f'{first} {last}'
    # print(addition['title'])
    for key,value in addition.items():
        print(key, value)
    return name

name = famous_name(first='Nahid', last='Hasan', title1='Enginner', title2='Cricketer')
print(name)