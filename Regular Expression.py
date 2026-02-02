import re

string1 = "Python is Fun Programming"
string2 = 'Twelve:12EightyNine:89SixtyNine:69'
string3 = 'hello 12 hi 89. World 34'
string4 = "Hello My Name is Python"
string5 = "Hello, World!"

pattern1 = r"\APython"
pattern2 = r"\d+"
pattern3 = r"\d+"
pattern4 = r"\s+"
replace = "SPACE"
pattern5 = r"Hello"

result1 = re.search(pattern1, string1)
result2 = re.split(pattern2, string2)
result3 = re.findall(pattern3, string3)
result4 = re.sub(pattern4, replace, string4)
result5 = re.subn(pattern4, replace, string4)
result6 = re.match(pattern5, string5)

print("Result 1 is [Search_Method] : ", result1)  # re.search()
print("Result 2 is [Split_Method] : ", result2)  # re.split()
print("Result 3 is [FindAll_Method] : ", result3)  # re.findall()
print("Result 4 is [Sub_Method] : ", result4)  # re.sub()
print("Result 5 is [Subn_Method] : ", result5)  # re.subn()
print("Start Index : ", result6.start())  # re.start()
print("End Index : ", result6.end())  # re.end()
print("Matched String is : ", result6.group())  # re.group()