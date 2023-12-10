import random

def generate_private_key(p):
  return random.randint(1,p-1)

def generate_public_key(p,g,private_key):
  return (pow(g,private_key)%p)

def generate_shared_key(private_key,public_key,p):
  return (pow(public_key,private_key) % p)

alice_private = generate_private_key(23)
alice_public = generate_public_key(23,9,alice_private)

bob_private = generate_private_key(23)
bob_public = generate_public_key(23,9,bob_private)

attacker_private = generate_private_key(23)
attacker_public = generate_public_key(23,9,attacker_private)

alice_shared = generate_shared_key(alice_private,attacker_public,23)
attacker_shared_alice = generate_shared_key(attacker_private,alice_public,23)

bob_shared = generate_shared_key(bob_private,attacker_public,23)
attacker_shared_bob = generate_shared_key(attacker_private,bob_public,23)

print("Shared Key Calculated by Alice = ",alice_shared)
print("Shared Key Calculated by Attacker with Alice= ",attacker_shared_alice)

print("\nShared Key Calculated by Bob = ",bob_shared)
print("Shared Key Calculated by Attacker with Bob= ",attacker_shared_bob)

if ((alice_shared == attacker_shared_alice) and (bob_shared == attacker_shared_bob)):
  print("Attacker has established a successful connection and can easily alter messages between Alice and Bob")
