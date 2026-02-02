import os
import shutil

# Define File Paths
Source_File = "Source.txt"
Destination_File = "Destination.txt"
New_Name = "Renamed.txt"

# Create a sample source file
with open(Source_File, "w") as f:
    f.write("This is a Sample File!")

# Renaming a File
print("Renaming File...")
try:
    os.rename(Source_File, New_Name)
    print(f"File Renamed to {New_Name}")
except FileNotFoundError:
    print(f"{Source_File} not found.")

# Moving a File
print("Moving a File...")
Destination_Directory = "Destination_Directory"
os.makedirs(Destination_Directory, exist_ok=True)  # Create directory if not exists
try:
    shutil.move(New_Name, Destination_Directory)
    print(f"File Moved to {Destination_Directory}")
except FileNotFoundError:
    print(f"{New_Name} not found.")

# Copying a File
print("Copying a File...")
try:
    shutil.copy(os.path.join(Destination_Directory, New_Name), ".")
    print("File Copied to Current Directory")
except FileNotFoundError:
    print("File to copy not found.")

# Removing a File
print("Removing a File...")
try:
    os.remove(os.path.join(Destination_Directory, New_Name))
    print(f"File Removed From {Destination_Directory}")
except FileNotFoundError:
    print("File to remove not found.")