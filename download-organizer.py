import os
import shutil

# Define the folder to organize
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# Define file type categories and their corresponding folders
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".dmg", ".sh", ".bat"],
    "Others": []
}

def organize_downloads():
    """Organize files in the Downloads folder into categorized subfolders."""
    # Ensure the Downloads folder exists
    if not os.path.exists(DOWNLOADS_FOLDER):
        print(f"Folder {DOWNLOADS_FOLDER} does not exist.")
        return

    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_folder = os.path.join(DOWNLOADS_FOLDER, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

    # Organize files into categories
    for item in os.listdir(DOWNLOADS_FOLDER):
        item_path = os.path.join(DOWNLOADS_FOLDER, item)

        # Skip directories
        if os.path.isdir(item_path):
            continue

        # Move files to the appropriate category folder
        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(item.lower().endswith(ext) for ext in extensions):
                shutil.move(item_path, os.path.join(DOWNLOADS_FOLDER, category, item))
                file_moved = True
                break

        # Move files with unknown extensions to "Others"
        if not file_moved:
            shutil.move(item_path, os.path.join(DOWNLOADS_FOLDER, "Others", item))

    print("Downloads folder organized successfully.")

if __name__ == "__main__":
    organize_downloads()