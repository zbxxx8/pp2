import os
def path_check(path):
    print(path,end='\n')
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))
path_check(r'C:\Users\Adm\Desktop\pp2\lab6\dir')
path_check(r'C:\Users\Adm\Desktop\pp2\lab6\files')
path_check(r'C:\Users\Adm\Desktop\pp2')