def combine(list1, list2):
    length_of_list_one = len(list1)
    length_of_list_two = len(list2)
    combination = []
    
    if length_of_list_one > length_of_list_two:
        for array in range(length_of_list_two):
            combination.append(list1[array])
            combination.append(list2[array])
        # Now add remaining elements from list1
        for remaining_index in range(array,length_of_list_one):
            combination.append(list1[remaining_index])

    elif length_of_list_one < length_of_list_two:
        array = 0
        for array in range(length_of_list_one):
            combination.append(list1[array])
            combination.append(list2[array])
        for remaining_index in range(array,length_of_list_two):
            combination.append(list2[remaining_index])
            
    else:
        if length_of_list_one == length_of_list_two:
            for array in range(length_of_list_one):
                combination.append(list1[array])
                combination.append(list2[array])
    return combination

print(combine([10,100,1000], [20,200,2000]))