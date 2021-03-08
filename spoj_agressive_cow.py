def largest_min_distance(arr,c,n):
    lb = 1
    hb = 1e9
    ans = 0

    while lb<=hb:
        previous = arr[0]
        cow=1
        mid = (hb+lb)//2
        for i in range(1,n):
            if arr[i]-previous>=mid:
                cow += 1
                previous=arr[i]
            if cow == c:
                break
        if cow==c:
            ans=mid
            lb=mid+1
        else:
            hb=mid-1
    print(int(ans))


if __name__=='__main__':
    T=int(input())
    while T:
        arr=[]
        n,c= map(int,input().split())
        for i in range(n):
            arr.append(int(input()))
        arr.sort()
        largest_min_distance(arr,c,n)
        T=T-1

