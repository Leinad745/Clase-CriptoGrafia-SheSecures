from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from PIL import Image
import os

def encriptar_imagen(inputPath, outputPath, key, modo):
    with Image.open(inputPath) as img:
        # Abre la imagen
        img = img.convert("RGB")
        size = img.size
        img_bytes = img.tobytes()

    # ECB y CBC
    if modo == AES.MODE_ECB:
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(AES.block_size))

    # Encriptar
    encrypted_data = cipher.encrypt(pad(img_bytes, AES.block_size))

    #Guardar el cifrado en bytes
    Image.frombytes("RGB", size, encrypted_data[:len(img_bytes)]).save(outputPath)

if __name__ == "__main__":
    src = "tux.png"
    key = get_random_bytes(16)
    encriptar_imagen(src, "tux_ecb.png", key, AES.MODE_ECB)
    encriptar_imagen(src, "tux_cbc.png", key, AES.MODE_CBC)