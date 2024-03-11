'''
Description: Ceasar Cipher impementation
 Author: Anas Ashraf
Email: anasashrafsadek@gmail.com
Date: 10/3/2024
'''


             #__process definition__#

def caesar_encrypt(plaintext,key):
  ciphertext=""

  for char in plaintext:
      if char in ALPHABET:
          ciphertext += ALPHABET[(ALPHABET.index(char)+key) %26]
  return ciphertext

def caesar_decrypt(ciphertext,key):
  plaintext=""

  for char in ciphertext:
      if char in ALPHABET:
          plaintext += ALPHABET[(ALPHABET.index(char)-key) %26]
  return plaintext



                        #__main program__#

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
operation= int(input("Enter 0 for Encryption\nOr 1 for Decryption\n"))
if not operation :
    plaintext = input("Enter plaintext: ")
    key = int(input("Enter Key: "))
    print(f"ciphertext:{caesar_encrypt(plaintext,key)}")
else:
    ciphertext = input("Enter ciphertext: ")
    key = int(input("Enter Key: "))
    print(f":{caesar_decrypt(ciphertext,key)}")

