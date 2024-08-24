from hashlib import sha256

def encrypt(key, message):
    message_bytes = message.encode()
    pad = sha256((str(0) + key).encode()).digest()
    ciphertext = bytearray()
    
    for i in range(len(message_bytes)):
        ciphertext.append(pad[i % len(pad)] ^ message_bytes[i])

    return bytes(ciphertext)

def decrypt(key, encrypted_message):
    pad = sha256((str(0) + key).encode()).digest()

    plaintext = bytearray()
    for i in range(len(encrypted_message)):
        plaintext.append(pad[i % len(pad)] ^ encrypted_message[i])
    
    return bytes(plaintext)