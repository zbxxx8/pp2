import re 
text="abb"
pattern=r'ab{2,3}'
print(re.search(pattern,text))