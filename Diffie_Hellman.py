import random

def generate_public_key(p,g,private_key):
  public_key = pow(g,private_key)
  public_key = public_key % p
  return public_key

def generate_shared_key(public_key,private_key,p):
  shared_key = pow(public_key,private_key)
  shared_key = shared_key % p
  return shared_key

p = int(input("Enter the value for p: "))
g = int(input("Enter the value for g: "))

alice_private_key = random.randint(1,p-1)
alice_public_key = generate_public_key(p,g,alice_private_key)

bob_private_key = random.randint(1,p-1)
bob_public_key = generate_public_key(p,g,bob_private_key)

shared_key_alice = generate_shared_key(bob_public_key,alice_private_key,p)
shared_key_bob = generate_shared_key(alice_public_key,bob_private_key,p)

if shared_key_alice == shared_key_bob:
  print("Success, shared key = ",shared_key_alice)
else:
  print("Failure")
