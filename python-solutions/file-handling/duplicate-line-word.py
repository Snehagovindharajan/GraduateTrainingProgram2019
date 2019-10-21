with open("find-duplicate.txt","r") as read_ptr:
    data = read_ptr.readlines()
    print(data)
    count_word = 0
    count_line = []
    count_dict = {}
    for i in data:
        if "topic" in i:
            count_word = count_word + i.count("topic")
            count_line.append(data.index(i))
            count_dict.update({data.index(i):i.count("topic")})
    print("count_word",count_word)
    print("count_line",count_line)
    print(count_dict)