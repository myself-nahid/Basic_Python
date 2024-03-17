""" def sum(num1, num2, num3=0):
    result = num1 + num2 +num3
    return result
total = sum(20, 30)
print(total) """

# variable number of
def sum(*numbers):
    print(numbers)
total = sum(20, 30, 50, 80, 100)
print(total)