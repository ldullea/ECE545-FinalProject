# Liam Dullea and Eric Mains
# ECE 545 UMass Amherst 
#
# Skeleton Code taken from Open Pyfhel Library found at: https://github.com/ibarrond/Pyfhel/tree/master


# Hash function used in main.py




import hashlib

def hash(password):
    
    str = hashlib.sha256(password.encode('utf-8'))
    text_hashed = str.hexdigest() 

    return text_hashed

if __name__ == '__main__' :
    passdigest = hash("Dullea")
    print(passdigest)
