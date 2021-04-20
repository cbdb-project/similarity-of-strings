'''Compare two strings by using each of their characters (Hongsu Wang)'''
from sims import compare_by_each_chars
output = compare_by_each_chars.compare("str1", "str2", [])
print(output)

'''Compare two strings by using each of substrings of candidate string (Linxu Wang)'''
from sims import compare_by_each_substrings
output = compare_by_each_substrings.compare("str1", "str12", ["str1"])
print(output)