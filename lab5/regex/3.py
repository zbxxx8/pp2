import re
pattern="\w*[_]\w*"
data="hello"
print(re.search(pattern,data))