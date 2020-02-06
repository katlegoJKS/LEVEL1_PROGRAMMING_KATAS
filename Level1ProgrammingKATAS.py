#Exercise: Hello
print("------TASK 1------")

def hello(name):
    print("Hello " + name)
hello("Tshepo!")



#Exercise: check if a number is even or odd
print("\n\n------TASK 2------")

def even_or_odd(numb):
    numb = int(input("Enter a number : "))
    if(numb%2==0):
        print("even")
    else:
        print("odd")
even_or_odd("numb")



#Exercise: Draw a square
print("\n\n------Task 3------")

def square(numb):
    numb = int(input("Enter a number: "))
    n_list = [["#" for x in range(numb)] for y in range(numb)]
    for row in range(0,numb):
        for col in range(0,numb):
                print(n_list[row][col],end=" ")
        print()
square("#")



#Exercise: Draw a right handed triangle
print("\n\n------Task 4------")

def triangle(Numbr): 
    Numbr = int(input("Enter a number: "))
    for i in range(1,Numbr+1):
        for j in range(1,i+1):
            print("#",end="")
        print()
triangle(2)



#Exercise: Draw an iscosceles triangle
print("\n\n------Task 5------")

def isosceles(num):
    num = int(input("Enter a number: "))
    row = 0
    while row<num:
        space = num-row-1
        while space>0:
            print(end=" ")
            space = space-1
        star = row+1
        while star>0:
            print("#",end=" ")
            star = star-1
        row = row+1
        print()
isosceles("")



#Exercise: Find the Longest string
print("\n\n------Task 6------")

def longestStr(word):
    print("The longest word(s) is: ")
    words = list(word.split(" "))
    length = [ ]
    for i in words:
        length.append(len(i))
    maximum = max(length)
    returnlist = []
    for j in words:
        if len(j) == maximum:
            returnlist.append(j)
            list_word = j
            print(list_word)
longestStr(input("Enter a sentence or series of words: "))



#Exercise: Combine two lists/arrays
print("\n\n------Task 7------")

arr1 = [1,10,100,1000]
arr2 = [2,20,200,2000]

n = len(arr1)
l = [ ]
def combine(arr):
    for i in range(n):
        l.append(arr1[i])
        l.append(arr2[i])
    print(l)
combine("")



#Exercise: Frame some text
print("\n\n------Task 8------")

p=input("Enter the sentence " + "'Write Good Code Every Day': ")
def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
frame(p.split(" "))