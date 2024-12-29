# Python Show Renamer

## Description

This script helps rename files in a directory by appending a season and episode format (e.g., `S01E01`) to their filenames. It is particularly useful for organizing TV show episodes or similar collections where consistent naming is required.

## Features

- Dynamically renames files in a specified directory.
- Prompts the user for a season number and appends it to filenames.
- Ensures user confirmation before performing file renaming.
- Handles errors such as non-existent directories gracefully.

---

## Prerequisites

Ensure you have Python 3.x installed on your system.

### Required Libraries

This script uses only standard Python libraries, so no additional installations are required.

---

## How to Use

### 1. Clone or download the script

Save the script to a local directory on your system.

### 2. Run the script

Run the script using Python:

```bash
python main.py
```

### 3. Provide inputs as prompted:

- **Directory Path:** Input the full path to the directory containing the files you want to rename.
- **Season Number:** Enter the season number (e.g., `1` for Season 1).

### 4. Confirm changes:

The script will display a mapping of the old filenames to the new filenames and prompt for confirmation. Type `y` to proceed or `n` to exit.

---

## Example Workflow

1. The script asks for the directory path:

   ```
   What directory do you want to rename files in? (Please use the full path): /path/to/files
   ```

2. The script asks for the season number:

   ```
   What season is this? 1
   ```

3. It displays the proposed changes:

   ```
   {'oldfile1.txt': 'S01E01.txt', 'oldfile2.txt': 'S01E02.txt'}
   These values are the old values with the new values. Would you like to continue? (y or n)
   ```

4. After confirmation, it renames the files and exits.

---

## File Structure

### Key Functions:

- **`cd` (Context Manager):** Temporarily changes the working directory.
- **`confirmUserInput`:** Ensures the user confirms before proceeding.
- **`getDirectoryAndSeason`:** Collects the directory path and season number from the user.
- **`getEpisodes`:** Extracts episode numbers from filenames.
- **`getSeasonAndEpisodesDictionary`:** Maps episode numbers to their new season-episode format.
- **`getNewFileNames`:** Prepares the old-to-new filename mapping.
- **`renameFiles`:** Renames files in the directory.

---

## Error Handling

- **Invalid Directory:** Alerts the user if the directory doesn't exist.
- **Invalid Season Input:** Prompts the user until a valid season number is entered.
- **User Abort:** Exits gracefully if the user decides not to proceed.

---

## Notes

- Ensure you have proper permissions to modify files in the target directory.
- Back up your files before running the script in case of unintended changes.

---

## License

This project is licensed under the MIT License.
