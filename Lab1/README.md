# Kriptografija zasnovana na simetričnom ključu 

Enkripcija simetričnim ključem se temelji na slijednim ili blok šiframa
* **Slijedne šifre** konzumiraju jedan po jedan bit
  * **Primjer:** **one-time pad** (iako neizvediva u većini primjena); **RC4** (ne koristi se); većina blok šifri se može pretvoriti u slijedne šifre korištenjem specijalnih modova.
* **Blok šifre** rade s porukama fiksne duljine
  * **Primjer:** *Data Encryption Standard* (**DES**) - ne koristi se, *Advanced Encryption Standard* (**AES**) - dizajniran kako bi jednako bio efikasan za softver i hardver te podupire rad s blokovima duljine 128 bitova i ključevima duljine 128, 192 i 256 bitova. U praksi je duzina skupa poruka koju treba procesirati puno duza od fiksnog bloka sa kojim radi sifra (npr., DES blok ima 64 bita). Blok šifra "razbije" ulaznu poruku u seriju sekvencijalnih blokova odgovarajuce dužine (npr. 128 bita), te procesira ove blokove po principu "jedan po jedan".

Ovisno o tome kako blok šifra procesira sekvencu blokova, postoje različiti modove rada blok sifri. Jedan od tih modova je i CBC mode.

Primjer blok šifre U CBC (*Cipher Block Chaining*) modu, svaki *plaintext* blok teksta se XOR-a s prethodnim *ciphertext* blokom blokom prje enkripcije. Na taj način, svaki *ciphertext* blok ovisi o svim prethodnim plaintext blokovima. Kako bi svaka poruka bila jedinstvena, za prvi blok treba koristiti nasumično generirani inicijalizacijski vektor. Kod CBC moda blok šifre (eng. *Block cipher*) rade sa blokovima fiksne duljine te zahtijevaju da je posljednji blok ispunjen sa *padding*-om ukoliko je njegova veličina manja od ukupne veličine bloka.

![CBC](https://user-images.githubusercontent.com/8695815/32179472-c9921c10-bd8f-11e7-85c8-1666f653835a.png)

U direktoriju [Studenti](Studenti) svakom studentu je dan file (secret.enc) enkriptiran korištenjem dole navedenog koda. Možete li ga dekriptirati?

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
