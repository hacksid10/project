def is_palindrome(number):
    original_number = str(number)
    reversed_number = original_number[::-1]
    return original_number == reversed_number

# Example usage
number = 121
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")