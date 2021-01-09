import binascii

def str2binary(str):
    return ' '.join(format(x, 'b') for x in bytearray(str, 'utf-8'))

def str2hex(str):
    s = str.encode().hex()
    return " ".join(s[i:i+2] for i in range(0, len(s), 2))
    
