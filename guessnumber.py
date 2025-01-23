import random
system_guess = random.randint(1, 99)
print("system number is: ", system_guess)
my_guess = []
while my_guess != 'd':
    my_guess = input()
    if my_guess == 'k':
        system_guess = random.randint(1, system_guess)
        print("system number is: ", system_guess)
        my_guess = input()
    elif my_guess == 'b':
        system_guess = random.randint(system_guess, 99)
        print("system number is: ", system_guess)
        my_guess = input()
    else:
        print('d')