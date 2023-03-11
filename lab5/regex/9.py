import re
example="HiMyNameIsZhansulu."
x=re.findall('[A-Z][a-z]*',example)
result=' '.join(x)
print(result)