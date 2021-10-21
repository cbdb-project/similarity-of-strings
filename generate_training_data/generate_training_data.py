import csv
from os import listdir
from os.path import isfile, join
import re

class file_operations:
    def open_csv(self, filename):
        def read_csv_by_line_number(line_number):
            nonlocal filename
            output = []
            with open(filename, "r", encoding="utf-8") as f_reader:
                csv_reader = csv.reader(f_reader, delimiter=",")
                for line in csv_reader:
                    output.append(line[line_number])
            return output
        return read_csv_by_line_number
    
    def open_dictionaries(self, dir_path):
        output = {}
        dictionaries = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
        for dictionary in dictionaries:
            filename = dictionary.split(".")[0]
            csv_line_reader = self.open_csv(f"{dir_path}\{dictionary}")
            content = csv_line_reader(0)
            output[filename] = content
        return output

    def write_csv(self, file_name, output_list):
        with open(file_name, 'w+', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(output_list)

def create_training_data_main(expressions, expression_answers, dictionary_list):
    output = [""]
    current_list = []
    output_for_single_expression = [[""]]
    current_combinations = []
    for expression_count in range(len(expressions)):
        expression = expressions[expression_count]
        answer = expression_answers[expression_count]
        print(f"working on: {expression}...")
        for expression_part in expression:
            if expression_part[0] =="[":
                dictionary_name = re.match("\[(.+)?\]", expression_part).groups()[0]
                if dictionary_name not in dictionary_list:
                    print(f"[{dictionary_name}] dictionary does not exist")
                    exit()
                else:
                    current_list_temp = dictionary_list[dictionary_name]
                    current_list = []
                    for term in current_list_temp:
                        if len(term)>2:
                            current_list.append(term[:-1])
                        else:
                            current_list.append(term)

            elif expression_part[-1] == "?":
                current_list = [expression_part[:-1],""]
            else:
                current_list = [expression_part]
            for combined_item in output_for_single_expression:
                for current_item in current_list:
                    if current_item == "" and len(combined_item[-1])==1:
                        continue
                    if combined_item!="" or current_item!="":
                        # current_combinations.append(f"{combined_item}{current_item}")
                        current_combinations.append(combined_item + [current_item])
            output_for_single_expression = current_combinations
            current_combinations = []
        # output_for_single_expression = ["".join(i) for i in output_for_single_expression]
        output_for_single_expression = [["".join(i), answer] for i in output_for_single_expression]
        output = output + output_for_single_expression
        output_for_single_expression = [[""]]
        output = [i for i in output if i !=""]
    return output

f_io = file_operations()
csv_line_reader = f_io.open_csv("expressions.csv")
expressions = [i.split("|") for i in csv_line_reader(0)]
expression_answers = csv_line_reader(1)
dictionary_list = f_io.open_dictionaries("dictionaries")
output_list = create_training_data_main(expressions, expression_answers, dictionary_list)
f_io.write_csv("output.csv", output_list)
print(output_list[:10])
