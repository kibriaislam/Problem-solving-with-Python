v = int(input())

a = int(input())

r = int(input())

p = int(input())

h = int(input())

if v+a+r>=h:
    print("WAW")
elif v+a+p>=h:
    print("WAW")
elif a+r+p>=h:
    print("WAW")
elif r+p+v>=h:
    print("WAW")
else:
    print("AWW")




