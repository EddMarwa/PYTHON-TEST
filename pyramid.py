def print_pyramid(x, row=1):
    if row > x:
        return
    
    print(' ' * (x - row), end='')
    print('* ' * row)
    print_pyramid(x, row + 1)

x = 7
print_pyramid(x)
