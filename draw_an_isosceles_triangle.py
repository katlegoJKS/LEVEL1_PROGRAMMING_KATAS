def isosceles_triangle(number_of_rows):
    isosceles_rows = ''
    number_of_rows = 2*number_of_rows -2

    for row_count in range(0,number_of_rows):
        for column in range(0,number_of_rows):
            print(end = " ")
        number_of_rows = number_of_rows-1
        for column in range(0,row_count+1):
            print("#", end = " ")
        print("\r")
    return isosceles_rows

print(isosceles_triangle(3))