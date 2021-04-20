import sys
def compare(str_1, str_2, algorithm_var):
    algorithm_var_str = algorithm_var[0]
    if algorithm_var_str == str_1:
        target = str_1
        candi_string = str_2
    elif algorithm_var_str == str_2:
        target = str_2
        candi_string = str_1
    else:
        print(f'please check the third parameter of your input')
        sys.exit()
    candi_list = [candi_string[i:i + x + 1] for x in range(len(candi_string)) for i in range(len(candi_string) - x)]
    for candi in candi_list:
        if len(candi)<len(target):pass
        elif target==candi:
            max_rate = len(target)/len(candi_string)
            break
        else:
            max_rate = 0
    return max_rate