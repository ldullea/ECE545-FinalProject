# Liam Dullea and Eric Mains
# ECE 545 UMass Amherst 
#
# Skeleton Code taken from Open Pyfhel Library found at: https://github.com/ibarrond/Pyfhel/tree/master
#
#
# 1. Imports and instantiation
# ---------------------------

import numpy as np
from Pyfhel import Pyfhel
HE = Pyfhel() 

# BGV Kep Setup

bgv_params = {
    'scheme': 'BGV',    # can also be 'bgv'
    'n': 2**13,         # Polynomial modulus degree, the num. of slots per plaintext,
                        #  of elements to be encoded in a single ciphertext in a
                        #  2 by n/2 rectangular matrix (mind this shape for rotations!)
                        #  Typ. 2^D for D in [10, 16]
    't': 65537,         # Plaintext modulus. Encrypted operations happen modulo t
                        #  Must be prime such that t-1 be divisible by 2^N.
    't_bits': 20,       # Number of bits in t. Used to generate a suitable value
                        #  for t. Overrides t if specified.
    'sec': 128,         # Security parameter. The equivalent length of AES key in bits.
                        #  Sets the ciphertext modulus q, can be one of {128, 192, 256}
                        #  More means more security but also slower computation.
}
HE.contextGen(**bgv_params)  # Generate context for bgv scheme
HE.keyGen()             # Key Generation: generates a pair of public/secret keys
HE.rotateKeyGen()       # Rotate key generation --> Allows rotation/shifting
HE.relinKeyGen()        # Relinearization key generation


integer1 = np.array([127], dtype=np.int64)
integer2 = np.array([-2], dtype=np.int64)
ctxt1 = HE.encryptBGV(integer1) # Encryption makes use of the public key
ctxt2 = HE.encryptBGV(integer2) # For BGV, encryptBGV function is used.
print("\n3. BGV Encryption, ")
print("    int ",integer1,'-> ctxt1 ', ctxt1)
print("    int ",integer2,'-> ctxt2 ', ctxt2)


ctxtSum = ctxt1 + ctxt2 
print("ctext sum:", ctxtSum)


ctxtSum = ctxtSum + 1

print("ctext sum:", ctxtSum)

resSum = HE.decryptBGV(ctxtSum)

print("     addition:       decrypt(ctxt1 + ctxt2) =  ", resSum)

