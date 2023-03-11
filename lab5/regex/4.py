import re
pattern=r"[A-Z]{1}[a-z]*"
text="Agwcdwcd"
print(re.search(pattern,text))