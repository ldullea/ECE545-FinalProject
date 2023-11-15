# Liam Dullea and Eric Mains
# ECE 545 UMass Amherst 
#
# Skeleton Code taken from Open Pyfhel Library found at: https://github.com/ibarrond/Pyfhel/tree/master
#
#
# 1. Imports and instantiation
# ---------------------------

import numpy as np
from hashtest import hash
from Pyfhel import Pyfhel

# HOMOMORPHIC ENCRYPTION INSTANTIATION 

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


# HASH LOGON INSTANTIATION
Users = []
check = True


# USER SECURE LOGON USING HASH FUNCTIONS

while check == True:
    error = 0
    username = ""
    password = ""
    print("\nEnter username and password (If new user enter \"NEW\")")
    username = input("Enter Username (case sensitive): ")
    if username == "NEW":
        newusername = input("Input new username (case sensitive): ")
        if newusername == "NEW":
                print("Username cannot be 'NEW' please enter new username")
                error = 1
            # DOUBLE CHECK CORNER CASE FOR OVERWRITING USERNAMES
        for user in Users:
            if user[0] == newusername:
                print("Error: duplicate username")
                error = 1
        if error == 1:
            continue
        newpassword = input("Enter new password (case sensitive): ")
        newpassdig = hash(newpassword)
        Users.append([newusername, newpassdig])
        #print("\n")
        #print(Users)
    elif(username == "EXIT"):
        exit()
    else:
        password = input("Enter Password (case sensitive): ")
        #print(Users)
        for user in Users:
            print(user)
            if user[0] == username and user[1] == hash(password):
                #print("HERE")
                check = False
                continue
            else:
                print("Incorrect Username/Password please try again\n")
                continue  
print("SUCCESSFUL LOGON")


# DEBUGGING AND TESTING 


#print(Users)

#test = hash("Dullea")

#print(test)


