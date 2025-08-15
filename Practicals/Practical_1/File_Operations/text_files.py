def create_and_write_files(filename):
    with open (filename,'w') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        file.write("This is the third line.\n")
create_and_write_files('sample.txt')
print("file created and written successfully.")

def read_and_print_file(filename):
    with open(filename,'r') as file:
        content = file.read ()
        print(content)
read_and_print_file('sample.txt')

def append_to_file(filename, newline):
    with open(filename,'a')as file:
        file.write(newline + "\n")
append_to_file('sample.txt', "This is the append line")
print("Line appended successfully.")
read_and_print_file('sample.txt')

def print_lines_with_numbers(filename):
    with open(filename, 'r') as file:
        for index, line in enumerate (file, start=1):
            print(f"{index}: {line.strip()}")
print_lines_with_numbers('sample.txt')

def count_words(filename):
    with open(filename,'r') as file:
        contents = file.read ()
        words = contents.split()
        return len(words)
Word_count = count_words('sample.txt')
print(f"The file contains {Word_count} words")
