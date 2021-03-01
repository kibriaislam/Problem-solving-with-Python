def reverse_string(sentence):
    word=sentence.split(" ")

    new_words=[words[::-1] for words in word ]

    newsentence = " ".join(new_words)

    
    return newsentence



def reversed_word(word):
    word=word[::-1]
    return word




def writing_file(sentence):
    with open('file.txt','w')as open_file:
        open_file.write(sentence)
        open_file.close()

    return

def read_file():
    with open('file.txt','r') as file_open:
        text=file_open.read()
    
    return text

def reverse_order(sentence):
    sentence=sentence.split(" ")
    sentence=sentence[::-1]
    sentence=" ".join(sentence)
    return sentence

print(reverse_order("kibria Islam "))


print(read_file())


writing_file("kibria Islam Otuno")

k=reverse_string("Kibria Islam")
print(k)



