def caesar_cipher_encrypt(text,key):
  result = ""
  for char in text:
    if char.isalpha():
      base = ord('A') if char.isupper() else ord('a')
      result += chr((ord(char)- base + key)%26 + base)
    else:
      result += char
  return result

def columnar_transposition_encrypt(message,key):
  n = len(key)
  message = message.replace(" ","").lower()
  message_len = len(message)
  
  padding_len = (n - (message_len % n)) % n
  padded_message = message + 'X' * padding_len
  
  grid = [['X'] * n for _ in range(n)]
  index = 0
  for row in range(n):
    for col in range(n):
      if index < len(padded_message):
        grid[row][col] = padded_message[index]
        index += 1
  
  for i in range(n):
    print(grid[i])

  encrypted_text = ""
  for col in key:
    for row in range(n):
        encrypted_text += grid[row][col - 1]

  return encrypted_text

def product_cipher(message,caesar_key,transposition_key):
  substitution = caesar_cipher_encrypt(message,caesar_key)
  final = columnar_transposition_encrypt(substitution,transposition_key)
  return final

print(product_cipher("Hello World this is Vineet",3,[4,1,2,3,5]))
