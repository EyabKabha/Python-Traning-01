def palindrome(str):
    if str==str[::-1]:
        print("True")
    else:
        print("False")

palindrome("helleh") # True
palindrome("kabha")  # False