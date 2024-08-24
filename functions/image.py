from .cryption import encrypt, decrypt
from PIL import Image

def encode(img, key, message):
    img = Image.open(img)
    img.save("new_image.jpg")
    encrypted_message = encrypt(key, message)

    with open("new_image.jpg", "ab") as image:
        image.write(encrypted_message)

def decode(img, key):
    with open(img, "rb") as img_file:
        message = img_file.read()
        end = bytes.fromhex("FFD9")
        encrypted_message = message[message.index(end) + len(end):]

    return decrypt(key, encrypted_message)
