# HelpfulScripts
 A bunch of helpful py scripts for increasing the efficiency of your work.


<details>
<summary>File Renaming Script</summary>

## File Renaming Script *namefiles.py*

### Overview
This script renames all files in a specified directory by giving them a consistent base name followed by a sequential number. The filenames are formatted with an underscore (_) and leading zeros (e.g., Ahtisaari1.jpg, Ahtisaari2.png). It also preserves the original file extensions and skips files without extensions.
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
    Ahtisaari_01.jpg
    Ahtisaari_02.png
    Ahtisaari_03.txt
```
### Customization
- Base Name: You can change the base_name variable in the script to use a different prefix for the renamed files.
- Directory Path: Update the directory variable to the path of your target folder.
</details>
