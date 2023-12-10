import hashlib

def Extended_Euclidian_GCD(a,b):
  if a == 0:
    return b,0,1
  gcd,x1,y1 = Extended_Euclidian_GCD(b%a ,a)
  x = y1 - (b//a)*x1
  y = x1
  return gcd,x,y

def modular_inverse(a,m):
  g,x,y = Extended_Euclidian_GCD(a,m)
  if g != 1:
    print("Modular Inverse does not exist")
    return 
  else:
    return x % m

def RSA_Signature(p,q,message):
  flag = True
  n = p*q
  phi = (p-1)*(q-1)
  e = 2
  while e < phi:
    GCD,_,_ = Extended_Euclidian_GCD(e,phi)
    if(GCD == 1):
      break
    else:
      e += 1
  
  d = modular_inverse(e,phi)
  hashed_message = hash(message)
  S = pow((hashed_message),d)
  S = S % n

  M1 = pow(S,e)
  M1 = M1 % n

  if M1 == message:
    flag = True
  return S,flag

