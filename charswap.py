



#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
def charswap(str1,str2):
    char1=str1[0]
    char2=str2[0]
    newstr=char2+str1[1:]+" "+char1+str2[1:]
    print(newstr)






if __name__=='__main__':
    charswap("abc","xyz")