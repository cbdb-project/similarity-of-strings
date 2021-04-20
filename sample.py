from sims import compare_by_each_chars
output = compare_by_each_chars.compare("str1", "str2", [])
print(output)

from sims import compare_by_each_substrings
output = compare_by_each_substrings.compare("str1", "str12", ["str1"])
print(output)