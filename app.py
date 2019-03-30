def unique_list(list):
    x=[]
    for i in list:
        if i not in x:
            x.append(i)
    print(x)

unique_list([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5])

"""
OUTPUT:
_______________
[1, 2, 3, 4, 5]

"""

def multiply(numbers):
    total=numbers[0]
    for x in numbers:
        total*=x
    print("total : ", total)

multiply([1,2,3,4,-5])


"""
OUTPUT:
_______________
total : -120

"""