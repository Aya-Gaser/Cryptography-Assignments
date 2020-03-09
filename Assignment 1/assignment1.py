import numpy as np
import sys 
import math

def get_outputFile_ready():
    file = open("output.txt", "w")
    file.truncate()
    file.close()

def getInput(input_file):
    f = open(input_file, "r")
    return f.read()

def split(word): 
    return [char for char in word]  

def writeOutput(text, file):
    f = open(file, "a")
    f.write(text)
    f.close()


def shift(operation, input_file, output_file, Key):
    cipher_list=[]
    key = int(Key)
    if operation == 'enc' or operation == 'encrypt':
        plaintext = getInput(input_file).upper() 
        splits = plaintext.split()
        #for loop to iterate over words array
        for splitt in splits:
            cipher_list=[]
            plaintext_list = split(splitt)
            for char in plaintext_list:
                plaintext_list = split(plaintext)
                ascci = ord(char) - 65
                print(ascci)
                cipher = np.mod((int(ascci) + key), 26)
                cipher_list.append(cipher)
            cipherText=''
            for ascci in cipher_list:
                char = chr(ascci+65)
                cipherText += char
            cipherText +='  '
            writeOutput(cipherText, output_file)

    elif operation == 'dec' or operation == 'decrypt' :
        plaintext_list =[]
        cipherText = getInput(input_file).upper()
        splits = cipherText.split()
        #for loop to iterate over words array
        for splitt in splits:
            plaintext_list=[]
            cipher_list = split(splitt)
            invrsKey = 26 - key
            for char in cipher_list:
                ascci = ord(char) - 65
                plain = np.mod((int(ascci) + invrsKey), 26)
                plaintext_list.append(plain)
            plaintext=''
            for ascci in plaintext_list:
                char = chr(ascci+65)
                plaintext += char
            plaintext+="  "
            writeOutput(plaintext, output_file) 

def getMultiInvrs(a, m=26):
    if math.gcd( a, 26) != 1:
        print('please enter a valid key !')
        return 
    else:
        a = a % m
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    


def affine(operation, input_file, output_file, key2, Key):
    cipher_list=[]
    key = int(Key)
    if operation == 'enc' or operation == 'encrypt':
        plaintext = getInput(input_file).upper()
        splits = plaintext.split()
        #for loop to iterate over words array
        for splitt in splits:
            cipher_list=[]
            plaintext_list = split(splitt)
            for char in plaintext_list:
                ascci = ord(char) - 65
                x = int(ascci) * int(key2)
                cipher = np.mod((x + key), 26)
                cipher_list.append(cipher)
            cipherText=''
            for ascci in cipher_list:
                char = chr(ascci+65)
                #print (char)
                cipherText += char
            cipherText+="  "
            writeOutput(cipherText, output_file)

    elif operation == 'dec' or operation == 'decrypt' :
        plaintext_list =[]
        cipherText = getInput(input_file).upper()
        print (cipherText)
        splits = cipherText.split()
        #for loop to iterate over words array
        for splitt in splits:
            #print(splitt).
            plaintext_list=[]
            cipher_list = split(splitt)
            #print (cipher_list)
            invrsKey = 26 - key
            invrsKey2 = int(getMultiInvrs(int(key2)))
            for char in cipher_list:
                ascci = ord(char) - 65
                x = invrsKey2*(int(ascci) + invrsKey)
                plain = np.mod(x, 26)
                plaintext_list.append(plain)
            plaintext=''
            for ascci in plaintext_list:
                char = chr(ascci+65)
                plaintext += char
            plaintext+=" "
            print(plaintext)
            writeOutput(plaintext, output_file)
             

        
def general(cipher, operation, input_file, output_file, key, key2=0):
    #print(cipher)
    if cipher == 'shift':
        #print(cipher)
        shift(operation, input_file, output_file, key)
    elif cipher == 'affine':
        #print(cipher)
        affine(operation, input_file, output_file, key, key2)





if __name__ == '__main__':
    get_outputFile_ready()
    n = len(sys.argv)
    if n == 6:
        general(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif n == 7:
        general(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    