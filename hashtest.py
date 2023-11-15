import hashlib


def hash(username, password):
    newpass = ''.join(str(ord(c)) for c in password)
    m = hashlib.sha256()
    m.update(b"(newpass)")
    
    digest = m.hexdigest()

    return digest

x = hash("Liam", "Hello")

print(x)