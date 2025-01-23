max1 = None  # Maximum value
max2 = None  # Second maximum value

x = int(input())  # First input
while x != -1:
    if max1 is None or x > max1:  # If x is greater than max1, update max1 and max2
        max2 = max1
        max1 = x
    elif max2 is None or x > max2:  # If x is greater than max2 but less than max1
        max2 = x
    x = int(input())  # Next input

if max1 is not None and max2 is not None:
    print(max1, max2)
