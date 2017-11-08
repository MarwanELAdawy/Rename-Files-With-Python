import os
def rename_files():
    file_list = os.listdir(r"Working Directory")
    #print (file_list)
    saved_path=os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"Working Directory")
    for file_name in file_list:
        print("Old Name - "+file_name)
        table = str.maketrans(dict.fromkeys('The Letters that you would remove it '))
        os.rename(file_name,file_name.translate(table))
    os.chdir(saved_path)
rename_files()
