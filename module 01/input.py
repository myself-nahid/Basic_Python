first_money = input("Bondu amare kisu taka de: ")
second_money = input("Bondu amre kisu taka de: ")
print(type(first_money))
# By Default the input from user will be string type
# typecasting
first_money_int = int(first_money)
second_money_int = int(second_money)
total_money = first_money_int + second_money_int
print("total money i got", total_money)
