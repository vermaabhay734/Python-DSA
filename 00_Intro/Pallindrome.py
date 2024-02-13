def isPalindrome(x):
    if (x < 0 or (x % 10 == 0 and x != 0)):
        return False
    
    rev = 0
    while(x>rev):
        last_digit = x % 10 
        rev = rev * 10 + last_digit
        x = x // 10

    if (x == rev or x == rev // 10):
        return True
    
    else:
        return False
    

abc = isPalindrome(1231)

print(abc)