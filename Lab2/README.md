# Hash funkcije 

U direktoriju [Studenti](Studenti) svakom studentu je dan file (secret.enc) čiji je sadržaj nastao kao rezultat hashiranja korisnikovig Prezimena, Imena i sedmeroznamenkastog (7) generiranog broja, (npr. *hash('Prezime Ime0123456')*). Možete li saznati o kojem se *random* broju radi (**HINT:** koristite brute-force).

**Napomena**: prilikom računanja hash-a nisu korištena slova abecede ćčžšđ i imenu i prezimenu.

U nastavku se nalazi kod za računanje *hash*-a.

```python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import itertools
import time
import random
import base64

PASS_SIZE = 7
PREZIME_IME = 'Perkovic Toni'

def calculateHash(student_name, randomNumber):
    toBeHashed = student_name + randomNumber
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

    if not isinstance(toBeHashed, bytes):
        toBeHashed = toBeHashed.encode()

    digest.update(toBeHashed)
    hash = digest.finalize()
    return base64.b64encode(hash)


if __name__ == '__main__':

    randomNumber = ''.join(str(x) for x in list(
        map(random.randrange, [10]*PASS_SIZE))
    )
    hash = calculateHash(PREZIME_IME, randomNumber)

    f_out = open("hashvalue", 'wb')
    f_out.write(hash)
    f_out.close()

    print(hash)
    print(randomNumber)
```
