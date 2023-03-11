import os
def path_check_filename(path):
    print(path)
    print('---'*20)
    if(os.access(path,os.F_OK)):
        print("PATH EXISTS!")
        print("Directory portion of the given path: ")
        print(os.path.dirname(path))
        print("Filename of the path is ")
        print(os.path.basename(path))
        
    else:
        print("PATH DOESNT EXIST!")
path_check_filename(r'C:\Users\Adm\Desktop\pp2\lab6\dir')
path_check_filename(r'C:\Users\Adm\Desktop\pp2\lab6\files')
path_check_filename(r'C:\Users\Adm\Desktop\pp2\22')