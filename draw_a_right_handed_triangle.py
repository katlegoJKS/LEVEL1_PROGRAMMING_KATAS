def right_handed_triangle(integer):
    right_angle_triangle_form = ''

    for row in range(abs(integer) + 1):
        print("#" * row)
    return right_angle_triangle_form

print(right_handed_triangle(4))