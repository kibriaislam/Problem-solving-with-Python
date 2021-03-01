
'''
Write a Python program to calculate the length of a string
'''

def length_of_string(string):
    count=0
    for char in string:
        count+=1
    print(count)




'''
Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
Sample String : google.com'
'''

def number_of_char(string):
    dic={}
    for char in string:
        key=dic.keys()
        if char in key:
            dic[char]+=1
        else:
            dic[char]=1
    print(dic)  


'''
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''

def making_string(string):
    if len(string)<=2:
        print("")
    else:
        print(string[:2]+ string[-2:])




#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself

def conversion(string):
    char=string[0]
    string=string.replace(char,'$')
    string=char+string[1:]
    print(string)

#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string
def charswap(str1,str2):
    char1=str1[0]
    char2=str2[0]
    newstr=char2+str1[1:]+" "+char1+str2[1:]
    print(newstr)



'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

def adding_ing_ly(string):

    if len(string)<3:
        print(string)
    else:
        if string[-3:]=="ing":
            string=string+"ly"
            print(string)
        else:
            string=string+"ing"
            print(string)




if __name__=='__main__':

    length_of_string("kibria Islam")
    number_of_char( "kinia islam")
    making_string("kibriaislam")
    conversion("kkkkkk111")
    charswap("abc","xyz")
    adding_ing_ly("kibriaislaming")
