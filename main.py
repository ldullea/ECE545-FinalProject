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

# Initialize Homomorphic encryption variables 

IntOption1 = np.array([0])
IntOption2 = np.array([0])
ctxtOption1 = HE.encryptBGV(IntOption1) # Encryption makes use of the public key
ctxtOption2 = HE.encryptBGV(IntOption2)


# initialize bootstrapping variables 
length = 2**n 
ZeroArray = np.zeros(length)
ZeroArray[0] = ZeroArray[0] + 1 

# HASH LOGON INSTANTIATION
Users = [["Liam",hash("Dullea")],["Eric",hash("Mains")],["Steve",hash("Jobs")],["Elon",hash("Musk")],["hello",hash("world")]]
Voted = {"Liam": 0,"Eric": 0,"Steve": 0,"Elon": 0,"hello": 0}
alreadyvoted = 0
NumberOfVoters = 0

# USER SECURE LOGON USING HASH FUNCTIONS
while True:
    while True:
        #Logon function
        check = True
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
            #print(newpassdig)
            Users.append([newusername, newpassdig])
            Voted[newusername] = 0
            print("New user successfully added")

            #print("\n")
            #print(Users)
        elif(username == "EXIT"):
            exit()
        else:
            password = input("Enter Password (case sensitive): ")
            #print(Users)
            for user in Users:
                #print(user)
                if user[0] == username and user[1] == hash(password):
                    #print("HERE")
                    if Voted[username] == 0:
                        print("SUCCESSFUL LOGON")
                        check = False
                    else:
                        alreadyvoted = 1
                    break
                else:
                    if username in Voted.keys():
                        if Voted[username] == 1:
                            alreadyvoted = 1 
                    continue
            if check == False:
                break
            if alreadyvoted == 1: 
                print("Error: User already voted")
            else:
                print("Incorrect Username/Password please try again\n") 
            alreadyvoted = 0
    
    # HOMOMORPHIC ENCRYPTION VOTING
    
    votecheck = False
    print("Do you prefer hot dogs or pizza?")
    while votecheck == False:
        vote = input("Enter 1 for option 1, enter 2 for option 2:")
        if vote == "1" or vote == "2":
            votecheck = True
    if vote == "1":
        ctxtOption1 = ctxtOption1 + 1
    if vote == "2":
        ctxtOption2 = ctxtOption2 + 1
    Voted[username] = 1

    NumberOfVoters = NumberOfVoters + 1

    if NumberOfVoters >= 5:
        break


resSum1 = HE.decryptBGV(ctxtOption1)
resSum2 = HE.decryptBGV(ctxtOption2)

if resSum1[0] > resSum2[0]:
    print("Option 1 Wins!", resSum1[0],"-", resSum2[0])    

if resSum1[0] < resSum2[0]:
    print("Option 2 Wins!", resSum1[0],"-", resSum2[0])    

if resSum1[0] == resSum2[0]:
    print("its a tie!", resSum1[0],"-", resSum2[0])    

# DEBUGGING AND TESTING 


#resSum1 = HE.decryptBGV(ctxtOption1)
#resSum2 = HE.decryptBGV(ctxtOption2)

#print(resSum1, resSum2)

#print(Users)

#test = hash("Dullea")

#print(test)


