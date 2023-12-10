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

  print("\nEncrypted Text = ",encrypted_text)
