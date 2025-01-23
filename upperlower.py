word = input()
words = word.split()
final = []
for word_ in words:
    capitalized_count = sum(1 for i in word_ if i.isupper())
    lower_count = sum(1 for i in word_ if i.islower())
    if capitalized_count > lower_count:
      final.append(word.upper())
    else:
      final.append(word.lower())
res = ' '.join(final)
print(res)
