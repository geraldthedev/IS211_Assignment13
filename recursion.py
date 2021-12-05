def fibonnaci(n):
    count = 0
    n1 , n2 = 0, 1
    if n == 0:
        print("Please enter a differnt number")
    else:
        while count <= n:
        
            fib = n1+n2
            n1 = n2
            n2 = fib
            count+=1
        print(fib)
    return fib

def gcd(a, b):

    if a == 0:
        return b
    r = b%a
    print(r)
    return r



def compareTo(s1, s2):
    if s1 < s2:
        val = -1
        print(val)
        return val
    if s1 == s2:
        print(0)
        return 0
    if s1 > s2:
        val2 = 1
        print(val2)
        return val2
    return

compareTo()
