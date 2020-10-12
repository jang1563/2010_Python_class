
def to_radix(n,b):
    if n<b:
        return str(n)
    s = to_radix(n/b, b)
    return s + str(n%b)


def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def up_down(s):
    print s
    if len(s)<=1:
        return
    up_down(s[:-1])
    print s
    
def palindrome(w):
    if len(w)<1:
        return True
    s = w[0] == w[-1]
    if not s:
        return False
    s = palindrome(w[1:-1])
    return s


    