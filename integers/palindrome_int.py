# Given an integer x, 
# return true if x is palindrome integer.

def isPalindromeStrConv(x: int) -> bool:
    if x < 0 or x - int(str(x)[::-1]) != 0:
        return False
    return True

# Can you solve the problem without converting x into a str?
def isPalindrome(x: int) -> bool:

    if x < 0:
        return False

    x_copy = x
    reverso = 0
    while x_copy > 0:
        reverso *= 10
        x_copy, remainder = divmod(x_copy, 10)
        reverso += remainder

    return not (reverso - x)