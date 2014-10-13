def unique_words_count(arr):
    my_dict = {}
    counter = 0
    for word in arr:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    for new in my_dict:
        counter += 1
    return counter

print(unique_words_count(["apple", "banana", "apple", "pie"]))
