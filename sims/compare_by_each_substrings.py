def compare(str_1, str_2, algorithm_var):
    if algorithm_var == str_1:
        target = str_1
        candi_string = str_2
    elif algorithm_var == str_2:
        target = str_2
        candi_string = str_1
    else:
        Print('please input the algorithm_var(string)!')
    candi_list = [candi_string[i:i + x + 1] for x in range(len(candi_string)) for i in range(len(candi_string) - x)]
    for candi in candi_list:
        if len(candi)<len(target):pass
        elif target==candi:
            max_rate = len(target)/len(candi_string)
            break
        else:
            max_rate = 0
    return max_rate
