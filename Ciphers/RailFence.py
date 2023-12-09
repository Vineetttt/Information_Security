def rail_fence_encrypt(text,rails):
  fence = [['\n' for _ in range(len(text))]for _ in range(rails)]
  row,direction = 0,1
  for i in range(len(text)):
    fence[row][i] = text[i]
    row += direction
    if row == rails - 1 or row == 0:
      direction *= -1

  encrypted_text = []
  for i in range(rails):
    for j in range(len(text)):
      if fence[i][j] != '\n':
        encrypted_text += fence[i][j]

  return ''.join(encrypted_text)


def rail_fence_decrypt(text,rails):
  fence = [['\n' for _ in range(len(text))]for _ in range(rails)]
  row,direction = 0,1

  for i in range(len(text)):
    fence[row][i] = '*'
    row += direction
    if row == rails - 1 or row == 0:
      direction *= -1

  index = 0
  for i in range(rails):
    for j in range(len(text)):
      if fence[i][j] == '*' and index < len(text):
        fence[i][j] = text[index]
        index += 1

  decrypted_text = ''.join(fence[i][j] for j in range(len(text)) for i in range(rails) if fence[i][j] != '\n')
  return decrypted_text
