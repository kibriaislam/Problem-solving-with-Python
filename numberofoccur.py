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


if __name__=='__main__':
    number_of_char("google")