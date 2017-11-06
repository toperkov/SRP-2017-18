# Hash funkcije 

U direktoriju [Studenti](Studenti) svakom studentu je dan file (secret.enc) čiji je sadržaj nastao kao rezultat hashiranja korisnikovig Prezimena, Imena i sedmeroznamenkastog (7) generiranog broja, (npr. *hash('Prezime Ime0123456')*). Možete li saznati o kojem se *random* broju radi (**HINT:** koristite brute-force).

**Napomena**: prilikom računanja hash-a nisu korištena slova abecede ćčžšđ i imenu i prezimenu.

U nastavku se nalazi kod za računanje *hash*-a.

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

	number_size = 7
	randomNumber = ''.join(str(x) for x in list(map(random.randrange, [10]*number_size)))
	hash = calculateHash('Prezime Ime', randomNumber)
	# kod kreiranja hasha nisu korištena slova abecede ćčžšđ,
	# odnosno umijesto npr. Perković se koristio Perkovic

	f_out = open("secret.enc", 'wb')
	f_out.write(hash)
	f_out.close()

	print(hash)
	print(randomNumber)
```
