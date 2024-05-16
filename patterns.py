def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

def right_triangle_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end=' ')
        print()


def inverted_right_triangle_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print()
def pyramid_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end=' ')
        for j in range(2*i+1):
            print('*', end=' ')
        print()
def inverted_pyramid_pattern(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(' ', end=' ')
        for j in range(2*i-1):
            print('*', end=' ')
        print()
def diamond_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end=' ')
        for j in range(2*i+1):
            print('*', end=' ')
        print()
    for i in range(n-2, -1, -1):
        for j in range(n-i-1):
            print(' ', end=' ')
        for j in range(2*i+1):
            print('*', end=' ')
        print()

def right_pascals_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end=' ')
        print()
    for i in range(n-1, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print()

def sandglass_pattern(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(' ', end=' ')
        for j in range(2*i-1):
            print('*', end=' ')
        print()
    for i in range(2, n+1):
        for j in range(n-i):
            print(' ', end=' ')
        for j in range(2*i-1):
            print('*', end=' ')
        print()

def hourglass_pattern(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(' ', end=' ')
        for j in range(i):
            print('*', end=' ')
        print()
    for i in range(2, n+1):
        for j in range(n-i):
            print(' ', end=' ')
        for j in range(i):
            print('*', end=' ')
        print()

def number_pyramid_pattern(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end=' ')
        for j in range(1, i+1):
            print(j, end=' ')
        for j in range(i-1, 0, -1):
            print(j, end=' ')
        print()



# Example usage:
print("Square Pattern")
square_pattern(5)

print("\nRight Triangle Pattern")

# Example usage:
right_triangle_pattern(5)

print("\nInverted Right Triangle Pattern")
inverted_right_triangle_pattern(5)

print("\nPyramid Pattern")
pyramid_pattern(5)

print("\nInverted Pyramid Pattern")
inverted_pyramid_pattern(5)

print("\nDiamond Pattern")
diamond_pattern(5)

print("\nRight Pascal's Triangle")
right_pascals_triangle(5)

print("\nSandglass Pattern")
sandglass_pattern(5)

print("\nHourglass Pattern")
hourglass_pattern(5)

print("\nNumber Pyramid Pattern")
# Example usage:
number_pyramid_pattern(5)
