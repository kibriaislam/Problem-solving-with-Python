def lower_bound(arr,k):
    l=0
    h=len(arr)
    while l< h:
        mid=(l+h)//2
        if k<=arr[mid]:
            h=mid
        elif k>arr[mid]:
            l=mid+1
    return l

def upper_bound(arr,k):
    l=0
    h=len(arr)
    mid=0
    while l<h:
        mid=(l+h)//2
        if k<arr[mid]:
            h=mid
        elif k>=arr[mid]:
            l=mid+1
    return h

T=int(input())
c=1
while T>0:
    x=list(map(int,input().split()))
    n=x[0]
    q=x[1]
    arr=list(map(int,input().split()))
    print("Case {}:".format(c))
    c += 1
    while q>0:
        y=list(map(int,input().split()))
        a=y[0]
        b=y[1]
        print(upper_bound(arr,b)-lower_bound(arr,a))
        q=q-1  
    T=T-1

