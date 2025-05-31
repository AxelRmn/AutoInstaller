# Automatic Software Installer

This project is a desktop tool developed in Python with a graphical interface (Tkinter) that automates the silent installation of essential software on Windows systems. It is ideal for enterprise environments, freshly formatted machines, or portable setups using a USB drive.

## Main Features

- Modern and intuitive graphical user interface
- Silent and unattended installation of multiple programs
- Detection of already installed software to avoid duplicates
- Detailed activity log (`logs/install_log.txt`)
- Automatic detection of portable mode (USB)
- Automatic installer updates via `updater.py`
- Uses relative paths (no absolute paths)

## Project Structure

```
AutoInstaller/
├── auto_installer.py               # Main script with GUI
├── updater.py                      # Script to download installers
├── requirements.txt                # Project dependencies
├── README.md                       # This documentation
├── .gitignore                      # Git exclusions
├── config/
│   └── software_list.json          # List of software to install
├── installers/                     # Manually added or downloaded installers
├── logs/
│   └── install_log.txt             # Automatically generated log
```

## Requirements

- Python 3.8 or higher
- Windows 10/11
- Internet connection (for `updater.py` usage)

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Use the Application

### Recommended Method: Graphical Interface

1. Run the main script:

```bash
python auto_installer.py
```

2. From the graphical window, you can:

- Select the software to install
- View real-time installation logs
- Download the latest installers with the **"Update Installers"** button

### Alternative: Run the updater manually

If you prefer to update installers from the terminal:

```bash
python updater.py
```

This will download the required `.exe` files to the `installers/` folder.

### (Optional) Generate the `.exe` file

To distribute the app without requiring Python:

```bash
pyinstaller --onefile --windowed auto_installer.py
```

The executable will be generated in the `dist/` folder.

## How to Add New Programs

To add new software to the project:

### 1. Edit the configuration file

Open `config/software_list.json` and add a new block like this:

```json
{
  "name": "Program Name",
  "installer_path": "installers/installer_name.exe",
  "silent_flag": "/S"
}
```

### (Optional) To enable automatic download, edit `updater.py`:

```
software = {
    "installer_name": "https://official.website/download.exe"
}
```

> Make sure to use the exact installer file name and the correct silent flag (e.g., /S, /silent, etc.).

## Portable Mode (USB)

You can copy the `AutoInstaller/` folder to a USB drive. If the program detects it is not running from drive `C:`, it will display:

> Portable mode detected (USB)

## Recommended .gitignore Exclusions

This project includes a `.gitignore` file that excludes:

- `/dist`, `/build`, `.exe`, `/logs`
- Virtual environments
- Temporary files and IDE settings

## Contributions

Contributions are welcome. If you'd like to improve this project, feel free to open an issue or submit a pull request following best development practices.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software, as long as you retain the author's name and the original MIT license in your distribution.
