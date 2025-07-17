# Write a Python function that checks if a number is even or odd and prints the result.
def check_even_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

#  A python function to check even or odd using bitwise operator
def check_even_odd_bitwise(number):
    # Check if the number is even or odd using bitwise AND
    if number & 1 == 0:
        print(f"{number} is even.[Using Bitwise Operator]")
    else:
        print(f"{number} is odd.[Using Bitwise Operator]")

# Example usage
user_value = int(input("Enter a number to check if it's even or odd: "))
check_even_odd(user_value)  # Outputs based on user input
check_even_odd_bitwise(user_value)  # Outputs: based on user input using bitwise operator

