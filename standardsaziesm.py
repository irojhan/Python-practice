names = []
for i in range(10):
  name = input()
  new = name.lower()
  final = new[0].upper() + new[1:]
  names.append(final)

for name_ in names:
  print(name_)
