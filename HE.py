# Liam Dullea and Eric Mains
# ECE 545 UMass Amherst 
#
# Skeleton Code taken from Open Pyfhel Library found at: https://github.com/ibarrond/Pyfhel/tree/master
#
# FILE FOR TESTING HOMOMORPHIC ENCRYPTION. NO ACTUAL IMPACT ON MAIN.PY









# 1. Imports and instantiation
# ---------------------------

import numpy as np
from Pyfhel import Pyfhel
HE = Pyfhel() 
n = 13 # modulus degree variable 
# BGV Kep Setup

bgv_params = {
    'scheme': 'BGV',    # can also be 'bgv'
    'n': 2**n,         # Polynomial modulus degree, the num. of slots per plaintext,
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


integer1 = np.array([0])
integer2 = np.array([0])
ctxt1 = HE.encryptBGV(integer1) # Encryption makes use of the public key
ctxt2 = HE.encryptBGV(integer2) # For BGV, encryptBGV function is used.
print("\n3. BGV Encryption, ")
print("    int ",integer1,'-> ctxt1 ', ctxt1)
print("    int ",integer2,'-> ctxt2 ', ctxt2)


ctxtSum = ctxt1 + ctxt2 
print("ctext sum:", ctxtSum)


votecount = 516096 # one hunred mil
print("Add", votecount, "to ciphertext")
ctxtSum = ctxtSum + votecount

print("ctext sum:", ctxtSum)

resSum = HE.decryptBGV(ctxtSum)


length = 2**n 
ZeroArray = np.zeros(length)
ZeroArray[0] = ZeroArray[0] + 1 
resSum = np.multiply(resSum, ZeroArray) 

print("     addition:       decrypt(ctxt1 + ctxt2) =  ", int(resSum[0]))


