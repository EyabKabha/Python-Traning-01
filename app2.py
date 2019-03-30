def up_low(s):
    d={"upper":0,"lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Orginal String : " , s)
    print("Number of Upper case characters : ",d["upper"])
    print("Number of Lower case characters : ",d["lower"])
s="Hello Mr . Rogers,How are you this fine Tuesday?"
up_low(s)

"""
OUTPUT:
_____________________

Orginal String :  Hello Mr . Rogers,How are you this fine Tuesday?
Number of Upper case characters :  5
Number of Lower case characters :  32

"""