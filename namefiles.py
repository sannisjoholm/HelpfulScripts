import os

# Set the directory
directory = "training/Ahtisaari"

# Give the name for the files
base_name = "Ahtisaari"

# Loop through the files in directory
for index, filename in enumerate(os.listdir(directory), start=1):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):  # Ensure it is a file
        # Extract the file extension to preserve it
        extension = os.path.splitext(filename)[1]
        new_name = f"{base_name}{index:1}{extension}"  # Format index with leading zeroes
        new_path = os.path.join(directory, new_name)
        os.rename(file_path, new_path)

print("Files are renamed!")