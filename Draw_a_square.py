def square(numbers):
    rows = ' '
    for row in range(numbers):
        for col in range(numbers):
                print('#', end ="")
        print()
    return rows

print(square(2))