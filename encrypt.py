def encrypt_letter(c, offset):
    if c.islower():
        if ord(c) + offset <= ord('z'):
            return chr( ord(c) + offset )
        else:
            return chr( ord(c) + offset - 26 )
    elif c.isupper():
        if ord(c) + offset <= ord('Z'):
            return chr( ord(c) + offset )
        else:
            return chr( ord(c) + offset - 26 )
    else:
        return c

def encrypt_msg(msg, offset):
    encrypted_msg = ""
    for c in msg:
        encrypted_msg += encrypt_letter(c, offset)
    return encrypted_msg

def decrypt_letter(c, offset):
    if c.islower():
        if ord(c) - offset >= ord('a'):
            return chr(ord(c)-offset)
        else:
            return chr( ord(c) - offset + 26)
    elif c.isupper():
        if ord(c) - offset >= ord('A'):
            return chr( ord(c) - offset )
        else:
            return chr( ord(c) - offset + 26)
    else:
        return c   

def decrypt_msg(msg, offset):
    decrypted_msg = ''
    for c in msg:
        decrypt_letter(c, offset)
    return decrypted_msg
