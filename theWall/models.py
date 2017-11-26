from django.db import models

# Create your models here.

'''
Function: rotn()

Description:
This function takes a character as input and shifts it forwards by "n" characters to generate a new character
that is within the alphabet
'''
def rotn(char, rot):
    char = chr((ord(char)+ord(rot) - 65))
    if ord(char) > ord('Z'):
        val = ord(char) - ord('Z')
        val = val + (ord('A') - 1)
        char = chr( val )

    return char

'''
Function: rotBack()

Description:
This function takes a character as input and shifts it backwards by "n" characters to generate a new character
that is within the alphabet
'''
def rotBack(char, rot):
    char = chr((ord(char) - (ord(rot) - 65)))

    if ord(char) < ord('A'):
        val = ord(char) + ord('A')-1
        if val > 97:
            val = val - 38
        char = chr(val)
    return char


'''
Function: vigEncrypt()

Description:
This function takes plaintext and a key as input. It uses the key to implement polyalphabetic substitution
to transform the plaintext into unintelligible ciphertext. The key is transformed to be as long as the message,
and each character in the message is rotated by the "n" characters according to the value of the key.
'''
def vigEncrypt(plainText, key):
    plainText = plainText.upper()
    key = key.upper()
    keyAry = []
    cipherText = []
    msgLen = len(plainText)
    keyLen = len(key)

    for i in range(msgLen):
        keyAry.append(key[i%keyLen])

    for i in range(msgLen):
        cipherText.append(rotn(plainText[i], keyAry[i]))
    return "".join(cipherText)


'''
Function: vigDecrypt()

Description:
This function does the opposite operation of vigEncrypt. It takes ciphertext and a key as input.
it uses the key to do a reverse rotation on all the characters in the text to try to decrypt them to their
original characters.
'''
def vigDecrypt(cipherText, key):
    key = key.upper()
    plainText = []
    keyAry = []
    msgLen = len(cipherText)
    keyLen = len(key)

    for i in range(msgLen):
        keyAry.append(key[i%keyLen])

    for i in range(msgLen):
        plainText.append(rotBack(cipherText[i], keyAry[i]))

    return "".join(plainText)

'''
Function: Post()

Description:
This is a django specific class. It is a model that is represented in the database. 
This particular model stores the "posts" that each person makes to the website.
'''
class Post(models.Model):
    content = models.CharField(max_length=280)
    key = models.CharField(max_length=140)

    def __str__(self):
        return self.content
