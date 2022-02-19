# StegoXOR
A small tool for stegano using XOR

This tool should be used to :
1. encrypt a file using xor and key file of same size
2. decrypt a file encrypted using xor with key file (you must have that keyfile and key file needs to be of the same size as encrypted file)

usage : python3 stegaxor.py -e|-d <file|cypherfile> <keyfile> <outputfile>

options :
    -e  --encrypt   Encrypt <file> by xoring it with <keyfile> and generate <outputfile>
    -d  --decrypt   Decrypt <cypherfile> by xoring it with <keyfile> and returning result
                    in <outputfile>
