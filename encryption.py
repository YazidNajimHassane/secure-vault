from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad , unpad
from dotenv import load_dotenv
import os

load_dotenv()
key= os.environ.get('AES_KEY').encode()


#encryption fonction
def encrypt_password(data):
    cipher=AES.new(key,AES.MODE_CBC)
    iv=cipher.iv
    ciphertext=cipher.encrypt(pad(data.encode(),AES.block_size))
    return iv , ciphertext

#decryption fonciton
def decrypt_password(iv , ciphertext):
    cipher = AES.new(key,AES.MODE_CBC,iv=iv)
    plaintext=unpad(cipher.decrypt(ciphertext),AES.block_size)
    return plaintext.decode()
