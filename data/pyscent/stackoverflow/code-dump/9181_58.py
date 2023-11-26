def encrypt(plainText,key):
    
    aes = AES.new(key, AES.MODE_ECB)    
    encrypt_aes = aes.encrypt(pad(plainText))   
    encrypted_text = str(base64.encodebytes (encrypt_aes), encoding = 'utf-8')
    return encrypted_text
