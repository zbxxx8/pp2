import re
pattern="\w*[_]\w*"
data="a_nurushev"
print(re.search(pattern,data))