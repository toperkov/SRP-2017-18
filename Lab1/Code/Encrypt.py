from cryptography.hazmat.primitives.ciphers import (
    Cipher,
    algorithms,
    modes
)
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64


BLOCK_SIZE = 32
CIPHER = algorithms.AES
CIPHER_BLOCK_LENGTH = 128
CIPHER_BLOCK_LENGTH_BYTES = CIPHER_BLOCK_LENGTH // 8


def encrypt_CBC(key, iv, plaintext):
	padder = padding.PKCS7(CIPHER_BLOCK_LENGTH).padder()
	padded_plaintext = padder.update(plaintext)
	padded_plaintext += padder.finalize()

	ciphertext = iv
	ciphertext += _encrypt(padded_plaintext, key=key, mode=modes.CBC(iv))

	return ciphertext


def _encrypt(plaintext, **params):
	key = params.get('key')
	assert key, 'Encryption key is missing'

	mode = params.get('mode')
	assert mode, 'Encryption mode is missing'

	cipher = Cipher(CIPHER(key), mode, backend=default_backend())
	encryptor = cipher.encryptor()
	ciphertext = encryptor.update(plaintext)
	ciphertext += encryptor.finalize()
	
	return ciphertext


if __name__ =='__main__':

	with open('plain.jpg', 'rb') as f:
		data = f.read()

	key = os.urandom(BLOCK_SIZE)
	iv = os.urandom(CIPHER_BLOCK_LENGTH_BYTES)
	enc = encrypt_CBC(key, iv, data)

	f_out = open("secret.enc", 'wb')
	f_out.write(key)
	f_out.write(enc)
	f_out.close()