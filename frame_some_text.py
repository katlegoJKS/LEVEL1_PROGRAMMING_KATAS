sentence = "write good code every day"

def frame(words):
    word_length = len(max(words,key =len))
    
    print( '*' *(word_length+4))
    for word in words:
        print('* {a:{b}} *'.format(a=word, b=word_length))        
    print('*' * (word_length +4))

print(frame(sentence.split(" ")))