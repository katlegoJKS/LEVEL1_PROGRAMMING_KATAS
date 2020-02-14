def Longest_word(word):
    longest_word =' '
    words = list(word.split(" "))
    lenght =[]
    for i in words:
        lenght.append(len(i))
    LongestString = max(lenght)
    returnlist = []
    for j in words:
        if len(j)==LongestString:
            returnlist.append(j)
            list_word = j
            print(list_word)
    return longest_word
    
Longest = Longest_word("the quick brown fox ate my chicken")

print(Longest)