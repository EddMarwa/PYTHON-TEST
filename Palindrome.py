def palindrome(p):
    p = p.replace(" ", "").lower()
    
    reversed_p = p[::-1]
    if p == reversed_p:
        return True
    else:
        return False
input_str = "Racecar"
if palindrome(input_str):
    print(f'"{input_str}" is a palindrome.')
else:
    print(f'"{input_str}" is not a palindrome.')