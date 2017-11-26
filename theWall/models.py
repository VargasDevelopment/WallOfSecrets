from django.db import models

# Create your models here.


def rotn(char, rot):
    char = chr((ord(char)+ord(rot) - 65))
    if ord(char) > ord('Z'):
        val = ord(char) - ord('Z')
        val = val + (ord('A') - 1)
        char = chr( val )

    return char


def rotBack(char, rot):
    char = chr((ord(char) - (ord(rot) - 65)))

    if ord(char) < ord('A'):
        val = ord(char) + ord('A')-1
        if val > 97:
            val = val - 38
        char = chr(val)
    return char


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


class Post(models.Model):
    content = models.CharField(max_length=280)
    key = models.CharField(max_length=140)

    def __str__(self):
        return self.content
