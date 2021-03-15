def marge(a,b,n,m):
    i,j,k=0,0,0
    c=[None]*10
    while(i<n and j<m):
        if(a[i]<=b[j]):
            c[k]=(a[i])
            k+=1
            i+=1
        else:
            c[k]=(b[j])
            k+=1
            j+=1
    
    while(i<n):
        c[k]=(a[i])
        k+1
        i+=1
    while(j<m):
        c[k]=(b[j])
        k+=1
        j+=1
    return c







if __name__=='__main__':

    a=[1,5,8,9,12]
    b=[2,6,10,11,13]
    n=len(a)
    m=len(b)


    result=marge(a,b,n,m)
    print(result)