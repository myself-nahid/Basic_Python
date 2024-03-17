""" 
Given a number N. Print the digits of that number from right to left separated by space. 
"""
def print_digits_from_right_to_left(N):
    digits = list(str(N))
    print(' '.join(digits[::-1]))

# Example usage
N = int(input("Enter a number: "))
print_digits_from_right_to_left(N)
