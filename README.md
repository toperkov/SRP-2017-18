# Symmetric Key Encryption

## Symmetric-key encryption is based on either stream ciphers or block ciphers.

* Stream ciphers consume the message one bit at a time
  * Examples: the legendary one-time pad (though unfeasible for most applications); RC4 (deprecated); most block ciphers can be turned into stream ciphers using special modes of operation (read on).
* Block ciphers operate on fixed-length blocks
  * Examples: Data Encryption Standard (DES) - deprecated, AES (Advanced Encryption Standard) - designed to be efficient in both hardware and software, and supports a block length of 128 bits and key lengths of 128, 192, and 256 bits.

Block ciphers have one or more block size(s) but, during transformation, the block size is always fixed. Block cipher modes operate on whole blocks and require that the last part of the data be padded to a full block if it is smaller than the current block size. There are, however, modes that do not require padding because they effectively use a block cipher as a stream cipher; such ciphers are capable of encrypting arbitrarily long sequences of bytes or bits.

Most block cipher modes require a unique binary sequence, often called an initialization vector (IV), for each encryption operation. The IV has to be non-repeating and, for some modes, random as well. The initialization vector is used to ensure distinct ciphertexts are produced even when the same plaintext is encrypted multiple times independently with the same key.

In CBC (Cipher Block Chaining) mode, each block of plaintext is XORed with the previous ciphertext block before being encrypted. This way, each ciphertext block depends on all plaintext blocks processed up to that point. To make each message unique, a random initialization vector must be used in for first block.

The file was encrypted using the following code. Can you decrypt it?

