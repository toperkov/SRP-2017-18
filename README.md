# Symmetric Key Encryption

Symmetric-key encryption is based on either stream ciphers or block ciphers.
* Stream ciphers consume the message one bit at a time
  * Examples: the legendary one-time pad (though unfeasible for most applications); RC4 (deprecated); most block ciphers can be turned into stream ciphers using special modes of operation (read on).
* Block ciphers operate on fixed-length blocks
  * Examples: Data Encryption Standard (DES) - deprecated, AES (Advanced Encryption Standard) - designed to be efficient in both hardware and software, and supports a block length of 128 bits and key lengths of 128, 192, and 256 bits.

Block ciphers have one or more block size(s) but, during transformation, the block size is always fixed. Block cipher modes operate on whole blocks and require that the last part of the data be padded to a full block if it is smaller than the current block size. There are, however, modes that do not require padding because they effectively use a block cipher as a stream cipher; such ciphers are capable of encrypting arbitrarily long sequences of bytes or bits.

Most block cipher modes require a unique binary sequence, often called an initialization vector (IV), for each encryption operation. The IV has to be non-repeating and, for some modes, random as well. The initialization vector is used to ensure distinct ciphertexts are produced even when the same plaintext is encrypted multiple times independently with the same key.

In CBC (Cipher Block Chaining) mode, each block of plaintext is XORed with the previous ciphertext block before being encrypted. This way, each ciphertext block depends on all plaintext blocks processed up to that point. To make each message unique, a random initialization vector must be used in for first block.

![CBC](https://user-images.githubusercontent.com/8695815/32179472-c9921c10-bd8f-11e7-85c8-1666f653835a.png)

In [Lab1/Studenti](Lab1/Studenti) folder every student is given an file (secret.enc) encrypted using the following code. Can you decrypt it?

```python
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
```
