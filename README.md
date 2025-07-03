# Download Organizer

A Python script to automatically organize files in your Downloads folder (or any directory) by file type.

## Features

- **Automatic Sorting:** Moves files into folders like Images, Documents, Videos, Archives, and more.
- **Easy to Use:** Just run the script—no advanced setup required.
- **Customizable:** Easily change target folders or file type mappings.
- **Cross-Platform:** Works on Windows, Linux, and macOS.

## How It Works

This script scans your chosen directory, identifies file types by extension, and moves each file into a matching subfolder.

## Usage

1. **Clone this repository:**
    ```
    git clone https://github.com/Hardikjain09/download-organizer.git
    cd download-organizer
    ```

2. **Install requirements (if any):**
    ```
    pip install -r requirements.txt
    ```
    *(Skip this step if there is no requirements file)*

3. **Run the script:**
    ```
    python download-organizer.py
    ```
    By default, it works on your Downloads folder.  
    To organize a different folder, edit the script or pass the folder path as an argument (if supported).

## Example

**Before:**
Downloads/
resume.pdf
photo.jpg
song.mp3
archive.zip
download-organizer.py

**After:**
Downloads/
Documents/resume.pdf
Images/photo.jpg
Music/song.mp3
Archives/archive.zip
download-organizer.py


## Customization

- Change file type mappings by editing the dictionary in the script.
- Set a different target folder by modifying the `DOWNLOADS_PATH` variable.

## License

MIT

---

**Created by [Hardik Jain](https://github.com/Hardikjain09)**
