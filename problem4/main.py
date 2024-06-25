def find_max_sum_sub_array(k, arr):
    maxSum = sum(arr[:k])
    currentSum = maxSum
    for x in range (k,len(arr)):
        currentSum += arr [x] - arr [x-k]
        maxSum = max(maxSum,currentSum)
    return maxSum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8