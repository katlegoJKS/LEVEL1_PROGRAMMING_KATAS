def even_or_odd(number):
    even_number = "even"
    odd_number = "odd"
    if(number%2==0):
        return even_number
    else:
        return odd_number

result = even_or_odd(3)

print(result)