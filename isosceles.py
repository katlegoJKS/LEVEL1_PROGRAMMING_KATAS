def isosceles_triangle(row_number):
    iso_rows = ''
    row_number = 2*row_number -2

    for row_count in range(0,row_number):
        for column in range(0,row_number):
            print(end=" ")
        row_number = row_number-1
        for column in range(0,row_count+1):
            print("#", end=" ")
        print("\r")
    return iso_rows
check= isosceles_triangle(3)
print(check)