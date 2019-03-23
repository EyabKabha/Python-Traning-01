def count_primes(num):
    #Check for 0 or 1 input 
    if num<2:
        return 0
    ###############
    # 2 or greater 
    ###############

    #Store our prime numbers
    primes=[2]
    #Counter going up to the input num
    x=3
    while x <=num:
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2
    print(primes)
    return len(primes)

#Main
count_primes(100)

"""
OUTPUT:
____________________________________
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

"""
