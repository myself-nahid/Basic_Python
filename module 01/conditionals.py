# in, not in, is, is not
# <, >, <=, >=, !=
# and, or 

a = 5
boss = False
if a > 5:
    print("5 er besi")
elif a == 5:
    print("5 er soman")
else:
    print("5 er kom")

if boss is True:
    print("ekhoni kaj ta kore dissi")
else:
    print("porre kaj ta kore dibo")


coin = 'head'
# nested conditions
if boss == True:
    print("Boss apni joss")
    if coin == 'tail':
        print("Batting")
    else:
        print("Bowling")
        if 5 > 2 or boss != True:
            print("do something")
            if 8%2 == 0 and 5%2 == 1:
                print('8 is an even number')
else:
    print("you are loss not a boss")