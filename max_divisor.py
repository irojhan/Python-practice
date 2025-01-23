def maghsoom(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c

# Collect 20 numbers from the user
numbers = []
#print("Please enter 20 numbers:")
for _ in range(20):
    number = int(input())
    numbers.append(number)

# Variables to track the number with maximum divisors
max_divisors = 0
number_with_max_divisors = None

# Find the number with the maximum divisors
for num in numbers:
    divisor_count = maghsoom(num)
    if divisor_count > max_divisors:
        max_divisors = divisor_count
        number_with_max_divisors = num

print(number_with_max_divisors, max_divisors)
