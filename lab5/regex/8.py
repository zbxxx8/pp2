import re
example="UpperCaseLettersSplit"
example1="HelloWorldIAmHappy"


x=re.findall('[A-Z][a-z]*',example)
x1=re.findall('[A-Z][a-z]*',example1)

print(*x)
print(*x1)