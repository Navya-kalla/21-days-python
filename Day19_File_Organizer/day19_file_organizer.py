import os
import shutil

print("=" * 50)
print("📁 FILE ORGANIZER".center(50))
print("=" * 50)

# Get folder path
folder_path = input("Enter the folder path: ").strip()

# Check folder
if not os.path.exists(folder_path):
    print("❌ Folder not found!")
    exit()

print("✅ Folder found!")

# Get all items
files = os.listdir(folder_path)

# File type mapping
file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".jfif": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    ".pdf": "PDFs",

    ".mp3": "Music",
    ".wav": "Music",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".py": "Python Files",
    ".java": "Java Files",
    ".c": "C Files",
    ".cpp": "C++ Files",

    ".txt": "Text Files",

    ".doc": "Documents",
    ".docx": "Documents",

    ".ppt": "Presentations",
    ".pptx": "Presentations",

    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",

    ".csv": "CSV Files",

    ".zip": "Archives",
    ".rar": "Archives",

    ".html": "Web Files",
    ".css": "Web Files",
    ".js": "Web Files",

    ".json": "JSON Files",
    ".xml": "XML Files"
}

moved = 0
skipped = 0

# Create log file with UTF-8 encoding
with open("organizer_log.txt", "w", encoding="utf-8") as log_file:

    for file in files:

        full_path = os.path.join(folder_path, file)

        # Ignore folders
        if not os.path.isfile(full_path):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()

        folder_name = file_types.get(extension)

        # Unsupported file
        if folder_name is None:
            skipped += 1
            print(f"Skipping: {file}")
            log_file.write(f"Skipped: {file}\n")
            continue

        # Destination folder
        destination_folder = os.path.join(folder_path, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        destination_path = os.path.join(destination_folder, file)

        # Duplicate file
        if os.path.exists(destination_path):
            skipped += 1
            print(f"{file} already exists.")
            log_file.write(f"Already Exists: {file}\n")
            continue

        # Move file
        try:
            shutil.move(full_path, destination_path)
            moved += 1

            print(f"Moved {file} -> {folder_name}")
            log_file.write(f"Moved: {file} -> {folder_name}\n")

        except Exception as e:
            skipped += 1
            print(f"Couldn't move {file}")
            print(e)
            log_file.write(f"Error: {file} -> {str(e)}\n")

print("\n" + "=" * 40)
print("FILE ORGANIZATION SUMMARY")
print("=" * 40)
print(f"Files Moved   : {moved}")
print(f"Files Skipped : {skipped}")
print("=" * 40)

print("\nOrganization completed successfully!")
print("Log file saved as 'organizer_log.txt'")