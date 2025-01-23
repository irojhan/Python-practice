def makan(a, b, c):
  makanha = [a, b, c]
  position = sorted(makanha)
  min_makan= position[1]
  minmakan = abs(a - min_makan) + abs(b - min_makan) + abs(c - min_makan)
  return minmakan

values = input().split(' ')    
valuess = [int(x) for x in values]
res = makan(valuess[0],valuess[1],valuess[2])
print(res)
