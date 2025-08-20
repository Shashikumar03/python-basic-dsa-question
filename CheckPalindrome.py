
def check_palindrome(s):
    s=str(s)
    return s==s[::-1]


a=check_palindrome("121")
print(a)