def combine(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    combination = []
    
    
    if len1 > len2:
        for array in range(len2):
            combination.append(list1[array])
            combination.append(list2[array])
        # Now add remaining elements from list1
        for remaining_index in range(array,len1):
            combination.append(list1[remaining_index])
    elif len1 < len2:
        array = 0
        for array in range(len1):
            combination.append(list1[array])
            combination.append(list2[array])
        for remaining_index in range(array,len2):
            combination.append(list2[remaining_index])
    else:
        if len1 == len2:
            for array in range(len1):
                combination.append(list1[array])
                combination.append(list2[array])
    return combination

check = combine([10,100,1000], [20,200,2000])
print(check)