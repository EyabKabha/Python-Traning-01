try:
    f=open('testfile','w')
    f.write('write a test line')
except TypeError:
    print('There was a Type Error')
except OSError:
    print('Hey you an OS Error')
finally:
    print('I always run')

def ask_for_int():
        while True:
            try:
                result=int(input('Please provide number '))
            except:
                print('Whoops! That is not a number ')
                continue
            else:
                print('Yes Thank you')
                break
            finally:
                print('End of try/except/finally')
                print('I will always run at the end!')

ask_for_int()

