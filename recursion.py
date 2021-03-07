def recursive_forloop(l,N,arr):
    if l<N:
        recursive_forloop(l+1,N,arr)
        print(arr[l])






if __name__=='__main__':

    N= int(input())
    arr=list(map(int,input().split()))
    l=0
    recursive_forloop(l,N,arr)

