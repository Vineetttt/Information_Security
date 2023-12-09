def vernam(text,key):
  if len(text) != len(key):
    print("length of key must be equal to the input")
    return
  result = ""
  for i in range(len(text)):
    temp = chr(ord(text[i])^ord(key[i]))
    result += temp
  return result
