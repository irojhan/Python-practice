def pali(input_string):
  input_string=input_string.lower()
  if input_string==input_string[::-1]:
    return 'palindrome'
  return 'not palindrome'

res = pali(input())
print(res)
