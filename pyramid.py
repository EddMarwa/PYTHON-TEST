def print_pyramid(n, row=1):
    # Base condition
    if row > n:
        return
    
    # Print leading spaces
    print(' ' * (n - row), end='')
    
    # Print stars
    print('* ' * row)
    
    # Recursive call to print next row
    print_pyramid(n, row + 1)

# Example usage:
n = 5  # Height of the pyramid
print_pyramid(n)
