import random
low = 1
high = 99
while True:
  guess = random.randint(low, high)
  print(guess)
  feedback = input()
  if feedback=='k':
    high = guess -1
  elif feedback=='b':
    low = guess +1
  elif feedback=='d':
    break