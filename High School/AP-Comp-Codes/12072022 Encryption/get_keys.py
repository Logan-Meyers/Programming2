import rsa as rsa

print("Generating your public/private keypairs now . . .")
keys = rsa.generate_keypair()
print("Public key: ", keys[0])
print("Private key: ", keys[1])
print("Modulus: ",keys[2])

# 12132022
# 233
# 131
# public: 20257
# private: 6353
# modulus: 30523