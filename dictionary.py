
def dict_char_count(s):
    my_dict1 = {}
    my_dict2 = {}
    l = len(s)
    m = int(l/2)
    s1 = s[:m]
    s2 = s[m:]
    print(s1, s2)
    for char in s1:
        if char in my_dict1:
            my_dict1[char] = my_dict1[char] + 1
        else:
            my_dict1[char] = 1

    for char in s2:
        if char in my_dict2:
            my_dict2[char] = my_dict2[char] + 1
        else:
            my_dict2[char] = 1

    for key, value in my_dict1.items():
        print(key, value)

    print("")
    for key, value in my_dict2.items():
        print(key, value)


    return my_dict1

print(dict_char_count("xaxbbbxxgghhjjkkllooppttyy"))
