# write a python program to print the contents of the directory using the OS module
# search for the function that does that
import os

# Specify the directory (use '.' for the current directory)
directory = "."

# List and print the contents of the directory
contents = os.listdir(directory)
print("Contents of the directory:", contents)
