#To check if the file exists or not 
import os 
def file_exists(filename):
    return os.path.exists(filename)
print(f"'sample.txt' exists: {file_exists('sample.txt')}")
print(f"'nonexistent.txt' exists: {file_exists('nonexistent.txt')}")

#to rename a file 
import os 
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
rename_file ('sample.txt', 'renamed_sample.txt')
print("File Renamed Successfully")
print(f"'renamed_sample.txt'exists: {file_exists('renamed_sample.txt')}")

#To delete a file 
import os 
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted")
    else:
        print("{filename} doesn't exists")
delete_file("binary_sample.bin")

#To Create a new directory 
import os
def create_directory(directory_name):
    if not os.path.exists (directory_name):
        os.makedirs (directory_name)
        print(f"Directory {directory_name} successfully created!")
    else:
        print("Directory{directory_name} already exists!")
create_directory('New Folder')

#to list all the file in a directory 
import os 
def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)
print("Files in the current directory: ")
list_files('.')

#To copy a file form one location to another
import shutil
def copy_file(source,destination):
    shutil.copy2(source,destination)
    print(f"File copied from {source} to {destination}")
copy_file('renamed_sample.txt', 'New Folder/copied_sample.txt')

#To read CSV file and print its components
import csv
def read_csv_file(filename):
    with open (filename,'r', newline = '') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(','. join(row))
#Sample CSV file
with open ('sample.csv', 'w', newline='')as file:
    csv_writer = csv.writer (file)
    csv_writer.writerow(['Name:', 'Age:', 'City'])
    csv_writer.writerow(['Alice', '30', 'New York'])
    csv_writer.writerow(['Bobe', '25', 'Los Angeles'])

print ("Contents of sample.csv:")
read_csv_file('sample.csv')
