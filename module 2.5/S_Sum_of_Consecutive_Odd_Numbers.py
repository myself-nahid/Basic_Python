""" 
Given two numbers X and Y. Print the sum of all odd numbers between them, excluding X and Y.
 """
def sum_odd_numbers(X, Y):
    # Swap values if X is greater than Y
    if X > Y:
        X, Y = Y, X

    # Initialize the sum
    odd_sum = 0

    # Iterate over the range between X and Y (exclusive)
    for num in range(X + 1, Y):
        if num % 2 != 0:  # Check if the number is odd
            odd_sum += num

    return odd_sum

# Get user input for X and Y
X = int(input("Enter the first number (X): "))
Y = int(input("Enter the second number (Y): "))

result = sum_odd_numbers(X, Y)
print("Sum of odd numbers between", X, "and", Y, "is:", result)
