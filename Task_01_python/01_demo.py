mis = int(input("Enter your Number : "))
arr=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
if mis>=0 and mis<=9:
   print("Your number is ", arr[mis])
elif mis>=10 and mis<=99:
    total = 0
    while(mis):
        digit=mis%10
        total=total+digit
        mis=mis//10       
    print("sum digit is ", total)
elif mis>=100 and mis<=999:
    total=1
    while(mis):
        digit=mis%10
        total=total*digit
        mis=mis//10
    print("Mul Numbers is " ,total)    
else :
      print("number has more than 3 digits")