from pathlib import Path
import os

def show_files_folders():
    path = Path('')
    item = list(path.rglob('*'))
    for i, items in enumerate(item):
        print(f"{i+1}, : {items}")

        

def create_file():

    try:
        show_files_folders()
        file_name = input("Enter the file you want to create : ")
        p=Path(file_name)
        if not p.exists():
            with open(p,'w') as fs:
                data =  input('Enter the Data you want to write : ')
                fs.write(data)


        else:
           print('File Already Exists')

    except Exception as err:
        print(f"Error occured as {err}")


def read_file():
    try:

        show_files_folders()
        file_name=input("Enter the File you want to Read : ")
        p=Path(file_name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)

            print("Readed Successfully")
        
        else:
            print("The file you are trying to read doesn't exist")
    
    except Exception as err:
        print(f"Error Occured as {err}")


def update_file():
    try:
        show_files_folders()
        file_name = input("Enter the File you want to update : ")
        p=Path(file_name)
        if p.exists() and p.is_file():
            print("Enter 1 for Changing the name of the file : ")
            print("Enter 2 for rewriting the data in the file : ")
            print("Enter 3 for appending the data in the file : ")
            option =  int(input())

            if option == 1:
                input_name = input("Enter the new name for file : ")
                p2=Path(input_name)
                if not p2.exists():
                    p.rename(p2)
                


            elif option == 2:
                with open(p,'w') as fs:
                    data = input("enter your data to Overwrite in file : ")
                    fs.write(data)


            elif option == 3:

                with open(p,'a') as fs:
                    data = input("Enter the data you want to Update : ")
                    fs.write(" "+data)


    except Exception as err:
        print(f"Error Occured as {err}")

    
def delete_file():
    try:
        show_files_folders()
        name=input("Enter the file you want to Remove : ")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print(f"{name} deleted successfully")

        else:
            print(f"{name} file doesn't exists")
            
    except Exception as err:
        print(f"Error Occured as {err}")




print("Enter 1 for Creating a file : ")
print("Enter 2 for Reading a file : ")
print("Enter 3 for Updating a file : ")
print("Enter 4 for Deletion of file : ")

selection =  int(input());

if(selection==1):
    create_file()

elif(selection==2):
    read_file()

elif(selection==3):
    update_file()

elif(selection==4):
    delete_file()

else:
    print("Please Choose Correct Operation ")