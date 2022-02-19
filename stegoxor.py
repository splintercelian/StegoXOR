#!/usr/bin/python3

from PIL import Image
from pwn import *
from sys import argv

help_message = """

StegoXOR is a tool used to decrypt document by performing a xor operation between
a cipherfile (arg1) and a keyfile (arg2). Today it is setup only to be used with
image but might be extended for other types of file. Note that in order to perform
such operation cypherfile and keyfile needs to be of the same size

usage : python3 stegaxor.py -e|-d <file|cypherfile> <keyfile> <outputfile>

options :
    -e  --encrypt   Encrypt <file> by xoring it with <keyfile> and generate <outputfile>
    -d  --decrypt   Decrypt <cypherfile> by xoring it with <keyfile> and returning result
                    in <outputfile>

"""
# Encrypt and decrypt function are currently the same but might change later that's why
# they are separate
def encrypt(inFile,keyFile):
    return xor(inFile.tobytes(),keyFile.tobytes())

def decrypt(inFile,keyFile):
    return xor(inFile.tobytes(),keyFile.tobytes())

def main():

    if argv[1] not in ("-e","-d","--encrypt","--decrypt") or not argv[2] or not argv[3] or not argv[4]:
        print(help_message)
    else:
        inFile = Image.open(argv[2])
        keyFile = Image.open(argv[3])
        outFileName = argv[4]
        mode = inFile.mode
        size = inFile.size
        inFileFormat = inFile.format
        
        if argv[1] in ("-e","--encrypt"):
            outFile = Image.frombytes(mode,size,encrypt(inFile,keyFile))
        else:
            outFile = Image.frombytes(mode,size,decrypt(inFile,keyFile))

        outFile.save(outFileName, format=inFileFormat)

if __name__ == '__main__':
    main()