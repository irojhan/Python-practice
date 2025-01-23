text1 = input()
res = ''
vowels = 'aAoOiIeEuU'
for i in text1:
  if i not in vowels:
    res += '.' + i.lower()
print(res)
