def solution(n):
    i=0
    while(i*2020<=n):
        rem=n-(i*2020)
        if(rem%2021==0):
            print("YES")
            return
        i+=1
    print("NO")










if __name__=='__main__':
    t=int(input())

    while(t):
        n=int(input())
        solution(n)
        t-=1