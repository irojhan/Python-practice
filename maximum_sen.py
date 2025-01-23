maxi = None  # Initialize the maximum value as None
x = int(input())  # First input
while x != -1:  # Loop until the user enters -1
    if maxi is None or x > maxi:  # Update maxi if it's None or if x is larger
        maxi = x
    x = int(input())  # Next input

if maxi is not None:  # Print the maximum value if there were valid inputs
    print(maxi)
