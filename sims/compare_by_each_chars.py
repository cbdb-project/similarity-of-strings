def compare(str_1, str_2, algorithm_var):
    str_1_set = set(str_1)
    str_1_set_len = len(str_1_set)
    str_2_set = set(str_2)
    str_2_set_len = len(str_2_set)
    intersection_set = str_1_set.intersection(str_2_set)
    intersection_set_len = len(intersection_set)
    if(str_1_set_len != 0 and str_2_set_len != 0):
        max_rate = max(intersection_set_len/str_1_set_len, intersection_set_len/str_2_set_len)
    else:
        max_rate = 0
    return max_rate, [intersection_set_len, ";".join(intersection_set)]