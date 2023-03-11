import os
f=open('1.txt','r')
counter=0
for line in f.readlines():
    counter+=1
f.close()
print('Number of lines in "1.txt" is : '+str(counter))