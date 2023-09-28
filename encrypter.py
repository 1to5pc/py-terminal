def encode(text,ekey):
    encodedTxt=""
    for x in text:
        print(x)
        encodedTxt=encodedTxt+str(chr((ord(x)+ekey)))
    return encodedTxt

def decode(Etext,dkey):
    decodedTxt=""
    for x in Etext:
        print(x)
        decodedTxt=decodedTxt+str(chr((ord(x)+dkey)))
    return decodedTxt
testKey=2
testTxt="The quick brown fox jumps over the lazy dog. 0123456789"
encodedTEXT=encode(testTxt,testKey)
print(encodedTEXT)
print(decode(encodedTEXT,-2))