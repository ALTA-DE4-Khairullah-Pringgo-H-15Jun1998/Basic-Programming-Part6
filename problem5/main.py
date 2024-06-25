def remove_duplicates(array):
    if not array:
        return 0
    array_unique = 1
    for x in range (1,len (array)):
        if array[x] != array[array_unique - 1]:
            array[array_unique] = array[x]
            array_unique +=1
    return array_unique

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4