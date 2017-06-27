def palindrome(x) :
    s=str (x)
    if s == s[::-1] :
        return True
    else:
         return False

print(palindrome(1221))
    
