def abi(input_string):
  ab_index=input_string.find('AB')
  ba_index=input_string.find('BA')
  if ab_index != -1 and input_string.find('BA',ab_index + 2)!= -1:
    return 'YES'
  if ba_index != -1 and input_string.find('AB',ba_index + 2)!= -1:
    return 'YES'
  return 'NO'

res = abi(input())
print(res)
