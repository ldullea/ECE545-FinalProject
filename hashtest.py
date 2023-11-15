import hashlib

def hash(password):
    
    str = hashlib.sha256(password.encode('utf-8'))
    text_hashed = str.hexdigest() 

    return text_hashed

if __name__ == '__main__' :
    passdigest = hash("Dullea")
    print(passdigest)