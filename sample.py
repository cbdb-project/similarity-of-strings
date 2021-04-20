#  compare_by_each_chars - Hongsu Wang
#  Description:
#    Compare two strings by using each of their characters
#  Reference link:
#    None
#  Input:
#    The first two variables - the strings need to be compared - string
#    The third varible - the varibles for this algorithm - list
#  Output:
#    The first varible - similarity degree - number
#    The second varible - [how many characters matched, which characters matched] - list
from sims import compare_by_each_chars
output = compare_by_each_chars.compare("str1", "str2", [])
print(output)

#  compare_by_each_substrings - Linxu Wang
#  Description:
#    Compare two strings by using each of substrings of candidate string
#  Reference link:
#    None
#  Input:
#    The first two variables - the strings need to be compared - string
#    The third varible - which string is the target string (the third variable must same as the one of the first two variables)  - string
#  Output:
#    The first varible - similarity degree - number
from sims import compare_by_each_substrings
output = compare_by_each_substrings.compare("str1", "str12", "str1")
print(output)