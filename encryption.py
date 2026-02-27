from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad , unpad
from dotenv import load_dotenv
import os
import re

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


#Password_strength fonction
def check_Strength(password):
    score = 0
    feedback= []

    if len(password)>=8 :
        score +=1
    else:
        feedback.append("Too short (mi 8)")

    if re.search(r'[A-Z]',password) : 
        score+=1
    else:
        feedback.append("Add Uppercase latters")

    if re.search(r'[a-z]',password) : 
        score+=1
    else:
        feedback.append("Add Lowerrcase latters")

    if re.search(r'[0-9]',password) : 
        score+=1
    else:
        feedback.append("Add  numbers")

    if re.search(r'[&#~{}()[]|`\^@^$*<>:;!,§.%]',password) : 
        score+=1
    else:
        feedback.append("Add special characters")

    levels={1:"Very Weak" ,2:"Weak" ,3:"Fair" ,4:"Strong" ,5:"very Strong" }

    return levels[score] , feedback
    
    