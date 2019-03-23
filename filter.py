def check_even(number):
    return number % 2 ==0

mynums=[1,2,3,4,5,6]

print(list(filter(check_even,mynums))) # --> [2, 4, 6]

'''
filter -->
creates a list of elements for which a function returns true. Here is a short.
'''