# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range 
# [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 
# 64-bit integers (signed or unsigned).

def reverse(x: int) -> int:
    reverso = 0
    negative = -1 if x < 0 else 1
    x_copy = abs(x)

    # a*b > c iff a > c/b
    while x_copy != 0 and reverso < (2**31 -1)/10 and reverso > -2**31/10:
        reverso *= 10
        x_copy, remainder = divmod(x_copy, 10)
        reverso += remainder
    
    if x_copy:
        return 0
    
    return reverso * negative