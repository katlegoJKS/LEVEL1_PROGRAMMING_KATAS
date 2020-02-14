    #Exercise: Hello
print("------TASK 1------")

def hello(name):
    print("Hello " + name)

hello("Tshepo!")



#Exercise: check if a number is even or odd
print("\n\n------TASK 2------")

def even_or_odd(number):
    if(number%2==0):
        print("even")
    else:
        print("odd")

even_or_odd(3)



#Exercise: Draw a square
print("\n\n------Task 3------")

def square(numbers):
    n_list = [["#" for height in range(numbers)] for width in range(numbers)]
    for row in range(0,numbers):
        for col in range(0,numbers):
                print(n_list[row][col],end=" ")
        print()

square(2)



#Exercise: Draw a right handed triangle
print("\n\n------Task 4------")

def triangle(Numbr): 
    for side1 in range(1,Numbr+1):
        for side2 in range(1,side1+1):
            print("#",end="")
        print()

triangle(2)



#Exercise: Draw an iscosceles triangle
print("\n\n------Task 5------")

def isosceles(integer):
    integer = 4
    row = 0
    while row<integer:
        space = integer-row-1
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
    for each_letter in words:
        length.append(len(each_letter))
    maximum = max(length)
    returnlist = []
    for each_word in words:
        if len(each_word) == maximum:
            returnlist.append(each_word)
            list_word = each_word
            print(list_word)
longestStr("once upon a time")



#Exercise: Combine two lists/arrays
print("\n\n------Task 7------")

array1 = [1,10,100,1000]
array2 = [2,20,200,2000]

number_of = len(array1)
array0 = [ ]
def combine(array):
    for element in range(number_of):
        array0.append(array1[element])
        array0.append(array2[element])
    print(array0)
combine("")



#Exercise: Frame some text
print("\n\n------Task 8------")

phrase = "Write Good Code Every Day"
def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
frame(phrase.split(" "))