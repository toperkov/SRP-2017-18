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
