# HelpfulScripts
A bunch of helpful py scripts for increasing the efficiency of your work.

Open to see more info:
<details>
<summary>File Renaming Script</summary>

## File Renaming Script *namefiles.py*

### Overview
This script renames all files in a specified directory by giving them a consistent base name followed by a sequential number. The filenames are formatted with a name and the increasing number (e.g., Ahtisaari1.jpg, Ahtisaari2.png). It also preserves the original file extensions and skips files without extensions.
### Prerequisites
- Python 3.x installed on your system.
- A directory containing the files you want to rename.
### Usage
1. Take the file *namefiles.py* to your main folder of the project.
2. Take the files you want to rename into the subfolder.
3. Navigate to the project directory:
```bash
cd <project-directory>
```
4. Run the script
```bash
python namefiles.py
```

### Example
#### Before running the Script
```markdown
training/Ahtisaari/
    1.jpg
    2.png
    randomfile.txt
```
#### After Running the Script
```markdown
training/Ahtisaari/
    Ahtisaari1.jpg
    Ahtisaari2.png
    Ahtisaari3.txt
```
### Customization
- Base Name: You can change the base_name variable in the script to use a different prefix for the renamed files.
- Directory Path: Update the directory variable to the path of your target folder.
</details>
<details>
<summary>Renaming Files by Their Folders</summary>    
## Renaming Files by Their Folders
Added the reading of the folder names in the File Renaming Script.

### Overview
This script renames all files in a specified directory by giving them the directory name followed by a sequential number.

### Prerequisites
- Python 3.x installed on your system.
- A directory containing the files you want to rename.
### Usage
1. Take the file *NameFilesByDirectory.py* to your main folder of the project.
2. Take the files you want to rename into the named subfolder (The files will have the name of this folder in them).
3. Change the variable "mainFolder" to fit your use. This is the Main Folder above the folders with the named folders.
4. Navigate to the project directory:
```bash
cd <project-directory>
```
5. Run the script
```bash
python NameFilesByDirectory.py
```

### Example
#### Before running the Script
```markdown
training/Ahtisaari/
    1.jpg
    2.png
    randomfile.txt
training/Kallio/
    134.jpg
    242.png
    randomfile5.txt
```
#### After Running the Script
```markdown
training/Ahtisaari/
    Ahtisaari1.jpg
    Ahtisaari2.png
    Ahtisaari3.txt
training/Kallio/
    Kallio1.jpg
    Kallio2.png
    Kallio3.txt
```
### Customization
- Base Name: You can change the folder names to use a different prefix for the renamed files. No need to edit the code here.
- Directory Path: Update the directory variable "mainFolder" to the path of your target folder. This is the Main Folder above the folders with the named folders.
</details>
