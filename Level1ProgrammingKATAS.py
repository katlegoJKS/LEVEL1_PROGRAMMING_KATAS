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