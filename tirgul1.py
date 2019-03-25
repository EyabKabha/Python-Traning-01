def spy_game(nums): #define the function 
    code = [0,0,7,'x'] # list to check
    for num in nums:  #loop runs to all numbers in the list
        # [0,7,'x']
        # [7,'x']
        # ['x']  Length = 1 
        if num == code[0]: 
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5])) # True 
print(spy_game([1,0,2,4,0,5,7])) # True 
print(spy_game([1,7,2,0,4,5,0])) # False 

