import math

def GCD(a,b):
  if a == 0:
    return b
  return GCD(b%a, a)

def RSA(p,q,message):
  print("Original Message: ",message)
  n = p*q
  e = 2
  phi = (p-1)*(q-1)
  while (e < phi):
    if (GCD(e,phi) == 1):
      break
    else:
      e = e+1
  
  d = 2
  while True:
    if (d * e) % phi == 1:
        break
    d += 1

  print("Public Key = ",e)
  print("Private Key = ",d)

  # Encryption c = (msg ^ e) % n
  c = pow(message,e)
  c = math.fmod(c,n)
  print("Encrypted Message: ",c)

  # Decryption m = (c ^ d) % n
  m = pow(c,d)
  m = math.fmod(m,n)
  print("Decrypted Message: ",m)
