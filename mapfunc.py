#Using map function
def square(num):
    return num**2
my_nums=[1,2,3,4,5]

print(list(map(square,my_nums))) # --> [1, 4, 9, 16, 25]

def spilcer(mystring):
    if len(mystring) % 2 ==0:
        return 'Even'
    else:
        return mystring[0]

names=['Andy','Eve','Sally']

print(list(map(spilcer,names))) # --> ['Even', 'E', 'S']