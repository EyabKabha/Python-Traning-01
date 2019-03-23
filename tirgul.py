max=0
avg=0
sum=0
cnt=0
i=1
teacher=int(input("Hello Dear Teacher\nPlease Enter your amount students "))
while i<=teacher:
          num=int(input("Enter a grade -1 to exit "))
          if num==-1:
               print("program exit")
               break
          if num<=0:
               print("Enter again Invalid Input")
               continue
          sum+=num
          cnt+=1
          i+=1
          if num>max:
               max=num
print("sum Grades is ",sum) 
print("AVG Grades is ", sum/cnt)
print("Max Grade is ", max)
