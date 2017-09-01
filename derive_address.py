import sys
from ecdsa import SigningKey, SECP256k1
import sha3

hex_priv_key = input("Input private key (64 hex chars): ")

keccak = sha3.keccak_256()
priv = SigningKey.from_string(string=bytes.fromhex(hex_priv_key), 
                              curve=SECP256k1)
pub = priv.get_verifying_key().to_string()

keccak.update(pub)
address = keccak.hexdigest()[24:]

print("Private key:", priv.to_string().hex())
print("Public key: ", pub.hex())
print("Address:     0x" + address)

input()