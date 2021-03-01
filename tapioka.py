if __name__ == '__main__':
    n = input()
    words=["tapioka", "bubble"]
    count=0
    n=n.split()

    for word in words:
        while word in n:
            n.remove(word)
    
    if len(n)>0:
        newstring=" ".join(n)
        print(newstring)
    else:
        print("nothing")


    