def print_pyramid(n, row=1):
    # Base condition: If current row exceeds total rows, stop recursion
    if row > n:
        return
    
    # Calculate and print leading spaces to center the stars
    print(' ' * (n - row), end='')
    
    # Print stars with a space
    print('* ' * row)
    
    # Recursive call to print the next row
    print_pyramid(n, row + 1)

# Example usage:
n = 5  # Height of the pyramid
print_pyramid(n)
