def odd(l,n,j,arr):
    c=0
    if l==n:
        n=j
        return
    if arr[l]%2==0:
        c+=1
        arr[j]=arr[l]
        j+=1
    odd(l+1,n,j,arr)
    

if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    odd(0,n,j,arr)
    print(arr)



