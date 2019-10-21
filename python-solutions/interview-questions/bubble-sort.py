def BubbleSort(unsorted_list):
    for num in range(len(unsorted_list)-1,0,-1):
        # print("num",num)
        for i in range(num):
            # print("i",i)
            if unsorted_list[i] > unsorted_list[i + 1]:
                temp = unsorted_list[i + 1]
                unsorted_list[i + 1] = unsorted_list[i]
                unsorted_list[i] = temp
        # print(unsorted_list)
    print(unsorted_list)


# to_be_sorted = [14, 33, 27, 35, 10]
to_be_sorted = [54,26,93,17,77,31,44,55,20]
BubbleSort(to_be_sorted)
