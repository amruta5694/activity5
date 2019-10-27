import time
import string

import os
import os.path
import filecmp

from Crypto.PublicKey import RSA

pkfile = "exercise/rsa_key.pub"
skfile = "exercise/rsa_key"

def rsa_keygen():
    key = RSA.generate(4096);

    with open(skfile, 'wb') as f:
        f.write(key.exportKey('PEM'))

    pk = key.publickey()

    with open(pkfile, 'wb') as f:
        f.write(pk.exportKey('PEM'))


def rsa_encrypt(fname):
    with open(pkfile, 'rb') as f:
        sk = RSA.importKey(f.read(), 'PEM');

    with open(fname, 'r') as f:
        pt = f.read()
        if len(pt) > 128:
            pt = pt[:128]
        pt = pt.encode('ascii')

    ct = sk.encrypt(pt, 0)[0]

    with open(fname + '.enc', 'wb') as f:
        f.write(ct)

def rsa_decrypt(fname):
    with open(skfile, 'rb') as f:
        sk = RSA.importKey(f.read(), 'PEM');

    with open(fname + '.enc', 'rb') as f:
        ct = f.read()

    pt = sk.decrypt(ct).decode('ascii')
    with open(fname + '.dec', 'w') as f:
        f.write(pt)

alphabet = "abcdefghijklmnopqrstuvwxyz"
ex3_path = "exercise/ex3.enc"
fname = "file.txt"

# Generating permutations
permutation = ""
found = False
for i in alphabet:
    for j in alphabet:
        for k in alphabet:
            with open(fname,'w') as f:
                f.write(i+j+k)
            permutation = i+j+k
            rsa_encrypt(fname)
            found = filecmp.cmp(ex3_path,fname+".enc")
            os.remove(fname)
            os.remove(fname+".enc")
            if found:
                break
        if found:
            break
    if found:
        break
print(permutation)