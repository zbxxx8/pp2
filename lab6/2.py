str = "It Is Armans Bday"

lower = 0
upper = 0

for x in str:
    if(x.isupper()):
        upper = upper + 1
    if(x.islower()):
        lower = lower + 1

print("number of upper case letters: ", upper)
print("number of lower case letters: ", lower)
