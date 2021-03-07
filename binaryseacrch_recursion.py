def recursive_binary_search(arr,low,high,x):
    mid = (low+high)//2
    if low<=high:
        if x==arr[mid]:
            return mid
        if x>arr[mid]:
            return recursive_binary_search(arr,mid+1,high,x)
        if x<arr[mid]:
            return recursive_binary_search(arr,low,mid-1,x)

    return -1



if __name__=='__main__':

    arr=list(map(int,input().split()))
    x=int(input())

    low=0
    high=len(arr)-1

    result=recursive_binary_search(arr,low,high,x)

    if result==-1:
        print("not present")
    else:
        print('vale is at index  {}'.format(result))
    


