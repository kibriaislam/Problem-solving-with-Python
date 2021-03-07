def binary_search(arr, find):
    low = 0
    high= len(arr)-1

    while (low<=high):
        mid=(low+high)//2
        if find==arr[mid]:
            return True
        if find<arr[mid]:
            high=mid-1
        if find>arr[mid]:
            low=mid+1
    return False


if __name__=='__main__':
    arr=list(map(int,input().split()))
    find=int(input())
    print(binary_search(arr,find))


