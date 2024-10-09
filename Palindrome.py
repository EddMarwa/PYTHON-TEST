def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    
    # Reverse the string
    reversed_s = s[::-1]
    
    # Check if original and reversed strings are the same
    if s == reversed_s:
        return True
    else:
        return False

# Example usage:
input_str = "Racecar"
if is_palindrome(input_str):
    print(f'"{input_str}" is a palindrome.')
else:
    print(f'"{input_str}" is not a palindrome.')