import string, os, datetime

x = datetime.now()
a = x.strftime(str)


with open(a + ".txt", "w") as f:
       f.writelines(letter)