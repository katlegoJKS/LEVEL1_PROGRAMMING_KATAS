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

sentence = input("Enter words or a sentence: ")

words = sentence.split()

print(words,"\n")

long_word_length = len(words[0])

for i in words:
    word_length = len(i)
    if word_length > long_word_length:
        long_word_length = word_length
        currentword = i

print(currentword)



#Exercise: Combine two lists/arrays
print("\n\n------Task 7------")

def combine():
    arr1 = [1,10,100,1000]
    arr2 = [2,20,200,2000]
    arr = arr1 + arr2
    print(arr)
combine()



#Exercise: Frame some text
print("\n\n------Task 8------")

def frame(num1,num2):
    for col in range(1,num1+1):
        print(" ")
        for row in range(1,num2+1):
            if(col == 1 or col == num1 or row == 1 or row == num2):
                print("#",end="  ")
            else:
                print("H",end="  ")
num1 = int(input("Enter a number for columns: "))
num2 = int(input("Enter a number for rows: "))
msg = "Write\ngood\ncode\nevery\nday."
l = len(msg)
frame(num1,num2)
