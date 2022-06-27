from math import floor


def is_palindrome(str):
    str = str.lower()
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return is_palindrome(str[1:-1])

def is_palindrome_i(str): 
    str = str.lower()
    for pointer in range(floor(len(str)/2)):
        if str[pointer] != str[(-1 - pointer)]:
            return False
    return True    
    

print('expected F:', is_palindrome_i('palindrome'))
print('expected T:', is_palindrome_i('palindromemordnilap'))
print('expected T:', is_palindrome_i('palindromeemordnilap'))