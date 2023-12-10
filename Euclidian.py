def Euclidian_GCD(a,b):
  if a == 0:
    return b
  return Euclidian_GCD(b%a,a)
