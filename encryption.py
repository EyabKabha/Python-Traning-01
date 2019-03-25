import random
import string

def Encryption1():
    result2=[]
    for y in range(0,10):
          temp2=random.choice(string.ascii_letters) # Random character to encryption 
          temp3=ord(temp2)                          # Character encryption
          result2.append(temp3)                     # append to list
    print("after Encryption --> " , result2)                
    Decryption(result2) 

def Encryption2(mystr):
    result = []
    for i in mystr:
          temp=ord(i)
          result.append(temp)
    print("after Encryption --> " , result)
    Decryption(result)


def Decryption(mystring):
    result2 = []
    for i in mystring:
          flag=int(i) 
          flag=chr(i)
          result2.append(flag)
          
    print("after Decryption --> " , ' '.join(result2))
print("-----------------------------")
Encryption1()
print("-----------------------------")
str=input("Enter a sentence that you want to encrypted ")
print("-----------------------------")
Encryption2(str)
print("-----------------------------")

"""
OUTPUT:
_____________________________

-----------------------------
after Encryption -->  [72, 83, 74, 84, 113, 79, 79, 80, 120, 78]
after Decryption -->  H S J T q O O P x N
-----------------------------
Enter a sentence that you want to encrypted ariel
-----------------------------
after Encryption -->  [97, 114, 105, 101, 108]
after Decryption -->  a r i e l
-----------------------------

"""