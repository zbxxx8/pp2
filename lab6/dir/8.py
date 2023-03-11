import os
def remove_file(path):
    if(os.access(path,os.F_OK)):
        print(path+' - path exists!')
        os.remove(os.path.basename(path))
        print('the file is removed!')
    else:
        print(path+' - path doesnt exist:^(')
remove_file(r'C:\Users\Adm\Desktop\pp2\lab6\dir\del.txt')
remove_file(r'C:\Users\Adm\Desktop\pp2\lab6\dir\del3.txt')