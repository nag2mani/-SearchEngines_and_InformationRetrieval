# This file is for testing purpose.

import sys

def sum_of_two_numbers():
    # Check if two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        return
    
    # Parse command-line arguments as integers
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Please provide valid integer inputs")
        return
    
    # Calculate the sum
    result = num1 + num2
    
    # Print the result
    # print(f"The sum of {num1} and {num2} is: {result}")



    