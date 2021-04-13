def compare(char_1, char_2, algorithm_var):
    char_1_set = set(char_1)
    char_1_set_len = len(char_1_set)
    char_2_set = set(char_2)
    char_2_set_len = len(char_2_set)
    intersection_set = char_1_set.intersection(char_2_set)
    intersection_set_len = len(intersection_set)
    if(char_1_set_len != 0 and char_2_set_len != 0):
        max_rate = max(intersection_set_len/char_1_set_len, intersection_set_len/char_2_set_len)
    else:
        max_rate = 0
    return max_rate, [intersection_set_len, ";".join(intersection_set)]