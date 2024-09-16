# Define the function to create and write to a file
def create_and_write_file():
    try:
        # Task 1: Create the file in write mode and add three lines
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: Hello, world!\n")
            file.write("Line 2: Python file handling.\n")
            file.write("Line 3: Numbers like 12345 can be written too.\n")
        print("File created and written to successfully.")
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error: {e}")
    finally:
        print("Finished writing to file.\n")


# Define the function to read and display the contents of the file
def read_and_display_file():
    try:
        # Task 2: Open the file in read mode and display its contents
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error: {e}")
    finally:
        print("Finished reading the file.\n")


# Define the function to append more lines to the file
def append_to_file():
    try:
        # Task 3: Open the file in append mode and add three more lines
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: This is an appended line.\n")
            file.write("Line 5: Adding more content to the file.\n")
            file.write("Line 6: Appending numbers like 67890.\n")
        print("Successfully appended to the file.")
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error: {e}")
    finally:
        print("Finished appending to the file.\n")


# Call the functions
if __name__ == "__main__":
    create_and_write_file()        # Creates the file and writes three lines
    read_and_display_file()        # Reads and displays the file contents
    append_to_file()               # Appends more lines to the file
    read_and_display_file()        # Reads and displays the updated file contents
