# function to check whether a number is an armstrong or not

def arm(n):
    num=0
    n1=n
    while(n!=0):
        rem= n%10
        num+=rem**3
        n=n//10

    if num==n1: return True
    else:return False

