def caesar_cipher(text,key,encrypt=True):
  result = ""
  for char in text:
    if char.isalpha():
      base = ord('A') if char.isupper() else ord('a')
      result += chr((ord(char)- base + key)%26 + base) if encrypt else chr((ord(char)- base - key)%26 + base)
    else:
      result += char
  return result


def brute_attack_caesar(ciphertext):
  for shift in range(1,26):
    decrypted_text = caesar_cipher(ciphertext,shift,encrypt=False)
    print(decrypted_text)
