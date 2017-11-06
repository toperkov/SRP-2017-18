# Hash funkcije 

U direktoriju [Studenti](Studenti) svakom studentu je dan file (secret.enc) čiji je sadržaj nastao kao rezultat hashiranja korisnikovig Prezimena, Imena i sedmeroznamenkasto nasumično generiranog broja. Možete li saznati o kojem se broju radi (HINT: koristitie brute-force sedmeroznamenkastog broja).

```python
from cryptography.hazmat.primitives.ciphers import (
    Cipher,
    algorithms,
    modes
)
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
import os
import itertools
import time
import random
import base64

def calculateHash (student_name, randomNumber):
	toBeHashed = student_name + randomNumber
	digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
	digest.update(toBeHashed)
	hash = digest.finalize()
	return base64.b64encode(hash)

if __name__ == '__main__':

	pass_size = 7
	randomNumber = ''.join(str(x) for x in list(map(random.randrange, [10]*pass_size)))
	hash = calculateHash('Zovko Luka', randomNumber)

	f_out = open("secret.enc", 'wb')
	f_out.write(hash)
	f_out.close()

	print(hash)
	print(randomNumber)
```
