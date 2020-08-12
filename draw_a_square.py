def square(integer):
    rows = ' '

    for row in range(integer):
        for col in range(integer):
                print('#', end ="")
        print()
    return rows

print(square(4))