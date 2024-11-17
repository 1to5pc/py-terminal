"""
This module encloses encryption and decryption functions
"""

def encode(text,ekey):
    """ Encodes text using a given key """
    encoded_txt=""
    for x in text:
        print(x)
        encoded_txt=encoded_txt+str(chr((ord(x)+ekey)))
    return encoded_txt

def decode(text_encr,dkey):
    """ Encodes text using a given key """
    decoded_txt=""
    for x in text_encr:
        print(x)
        decoded_txt=decoded_txt+str(chr((ord(x)+dkey)))
    return decoded_txt

TEST_KEY=2
TEST_TXT="The quick brown fox jumps over the lazy dog. 0123456789"
ENCODEDTEXT=encode(TEST_TXT,TEST_KEY)
print(ENCODEDTEXT)
print(decode(ENCODEDTEXT,-2))