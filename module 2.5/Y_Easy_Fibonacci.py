""" 
Given a number N. Print first N numbers of the Fibonacci sequence.
 """

def fibonacci_sequence(n):
    # Check if n is 0 or negative
    if n <= 0:
        return []

    sequence = [0, 1]  # Initialize the sequence with the first two numbers

    # Generate Fibonacci sequence up to the desired length
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]

# Get user input for N
N = int(input("Enter the value of N: "))

fibonacci_numbers = fibonacci_sequence(N)
print("Fibonacci sequence up to", N, "numbers:", fibonacci_numbers)
