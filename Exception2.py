#example 1
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
     print('Type error! Watch out!')
finally:
    print('I always run')

#example 2
try:
    x=5
    y=0
    z=x/y
except ZeroDivisionError:
        print('Error!!')
finally:
        print('All Done!!')

#example 3
def ask():
    while True:
        try:
            n=int(input("Enter a number "))
        except:
            print('Please try again! \n')
            continue
        else:
            break
    print('Your number squared is : ')
    print(n**2)
ask()