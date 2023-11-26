def rot13_encrypt(text):
    return ''.join(chr((ord(letter) - ord('a') + 13) % 26 + ord('a')) for letter in text)
def rot13_decrypt(text):
    return ''.join(chr((ord(letter) - ord('a') - 13 + 26) % 26 + ord('a')) for letter in text)
rot13_encrypt('helloworld')
Out[22]: 'uryybjbeyq'
rot13_decrypt(rot13_encrypt('helloworld'))
Out[23]: 'helloworld'
