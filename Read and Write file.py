# Creating a File on Current Working Directory
file = open("MyFile.txt", "w+")  # using 'w+' to create a new file or overwrite existing
print("File is Successfully Created...!!")
print("Content of MyFile.txt is :")

# Read the Content of File Using file.read() method
print(file.read())

# Write the Content on File Using file.write() method
file.write("This is a Sample text of new File\n")  # \n is used for newline
print("Content Added Successfully...!!")

file.close()  # Close the File