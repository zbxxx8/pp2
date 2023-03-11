import os
path = r'C:\Users\Adm\Desktop\pp2\lab6\dir'
print("Only directories: ")
for item in os.listdir(path):
    if (os.path.isdir(os.path.join(path,item))):
        print(item,end=' ')
print('\n')
print("Only files: ")
for item in os.listdir(path):
    if(os.path.isfile(os.path.join(path,item))):
        print(item,end=' ')
print('\n')
print("All directories and files: ")
for item in os.listdir(path):
    print(item,end=' ')