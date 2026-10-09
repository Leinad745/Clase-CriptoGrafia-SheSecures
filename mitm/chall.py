# Desafío: "Doble candado" - doble cifrado AES con llaves débiles
#
#   C = E_K2( E_K1(P) )
#
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
import os

def derive(seed: bytes) -> bytes:
    return sha256(seed).digest()[:16]

K1 = derive(os.urandom(2))   # solo 2 bytes de entropía = 65.536 opciones
K2 = derive(os.urandom(2))

def E(K, x):                 # E_K(x): cifrar x con la llave K
    return AES.new(K, AES.MODE_ECB).encrypt(x)

P_flag = open(".flag.txt", "rb").read().strip()   # la flag NO viene en el código
P = pad(b"Hola, bienvenida!", 16)[:16]   # texto plano conocido (1 bloque)

C      = E(K2, E(K1, P))                 # C = E_K2(E_K1(P))
C_flag = E(K2, E(K1, pad(P_flag, 16)))   # C_flag = E_K2(E_K1(P_flag)): cifrada con las mismas llaves

print("P      =", P.hex())
print("C      =", C.hex())
print("C_flag =", C_flag.hex())
