def odd_divisor(n):
    while(n%2==0):
        n=n/2
    if n>1:
        print("YES")
    else:
        print("NO")
            






if __name__=='__main__':
    t=int(input())

    while(t):
        n=int(input())
        odd_divisor(n)
        t-=1
        