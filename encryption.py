from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad , unpad
from dotenv import load_dotenv
import os
import re

def validate_AES_key(key):
    if not key:
        raise ValueError("AES_KEY is not set in environment variables")
    key = key.encode()
    if len(key) not in (16, 24, 32):
        raise ValueError(f"AES_KEY must be 16, 24, or 32 bytes, got {len(key)} bytes")
    return key

load_dotenv()
key = os.environ.get('AES_KEY')
key = validate_AES_key(key)

#encryption function
def encrypt_password(data):
    cipher=AES.new(key,AES.MODE_CBC)
    iv=cipher.iv
    ciphertext=cipher.encrypt(pad(data.encode(),AES.block_size))
    return iv , ciphertext

#decryption function 
def decrypt_password(iv , ciphertext):
    cipher = AES.new(key,AES.MODE_CBC,iv=iv)
    plaintext=unpad(cipher.decrypt(ciphertext),AES.block_size)
    return plaintext.decode()


#Password_strength function
def check_Strength(password):
    score = 0
    feedback= []

    if len(password)>=8 :
        score +=1
    else:
        feedback.append("Too short (min 8 characters)")

    if re.search(r'[A-Z]',password) : 
        score+=1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r'[a-z]',password) : 
        score+=1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r'[0-9]',password) : 
        score+=1
    else:
        feedback.append("Add numbers")

    if re.search(r'[&#~{}()\'\[\]|`\\^@^$*<>:;!,§.%]',password) : 
        score+=1
    else:
        feedback.append("Add special characters")

    levels={1:"Very Weak" ,2:"Weak" ,3:"Fair" ,4:"Strong" ,5:"Very Strong" }

    if feedback==[]:
        feedback.append("✅")

    return levels[score] , feedback
