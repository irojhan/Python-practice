word = input()
index = 0
target = 'hello'
for char in word:
  if char == target[index]:
    index += 1
    if index == len(target):
      print('Yes')
      break
else:
  print('NO')
