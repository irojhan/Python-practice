def salam(input_string):
  target='hello'
  input_index=0
  for char in input_string:
    if char==target[input_index]:
      input_index+=1
      if input_index==len(target):
        return 'YES'
  return 'NO'

res = salam(input())
print(res)
