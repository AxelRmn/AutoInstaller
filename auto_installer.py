import json, subprocess, os, datetime, platform
import tkinter as tk
from tkinter import messagebox, scrolledtext
import winreg

# ----------------------------- Core Functions -----------------------------

def log(message):
    """Log messages to the GUI and to the install log file."""
    os.makedirs("logs", exist_ok=True)
    timestamp = f"{datetime.datetime.now()} - {message}\n"
    with open("logs/install_log.txt", "a", encoding="utf-8") as f:
        f.write(timestamp)

    log_area.config(state="normal") 
    log_area.insert(tk.END, timestamp)
    log_area.see(tk.END)
    log_area.config(state="disabled")  
    print(message)

def install_software(name, path, flag):
    """Run the silent installation command for the given software."""
    try:
        full_path = os.path.abspath(path)
        log(f"[>] Installing {name}...")
        cmd = f'start /wait "" "{full_path}" {flag}'
        subprocess.run(cmd, shell=True, check=True)
        log(f"[✔] {name} installed successfully.")
    except subprocess.CalledProcessError:
        log(f"[✖] Installation failed for {name}.")

def load_config():
    """Load software list from JSON configuration file."""
    with open("config/software_list.json", "r", encoding="utf-8") as f:
        return json.load(f)["software"]

def is_running_from_usb():
    """Determine whether the program is running from a USB drive."""
    current_drive = os.path.splitdrive(os.getcwd())[0]
    return current_drive.upper() != "C:"

def update_installers_from_gui():
    """Run the updater script to download the latest installers."""
    try:
        log("[~] Running updater script...")
        exit_code = os.system("python updater.py")
        if exit_code == 0:
            log("[✔] Installer update completed successfully.")
            messagebox.showinfo("Update Complete", "Latest installers have been downloaded.")
        else:
            log("[✖] Error occurred while running updater.")
            messagebox.showerror("Update Failed", "There was an error running updater.py")
    except Exception as e:
        log(f"[✖] Exception: {str(e)}")
        messagebox.showerror("Update Failed", f"An error occurred:\n{e}")

def is_software_installed(display_name):
    """Check the Windows Registry to see if the software is already installed."""
    registry_hives = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
    ]

    for hive, path in registry_hives:
        try:
            reg = winreg.OpenKey(hive, path)
            for i in range(winreg.QueryInfoKey(reg)[0]):
                subkey = winreg.EnumKey(reg, i)
                app_key = winreg.OpenKey(reg, subkey)
                try:
                    name = winreg.QueryValueEx(app_key, "DisplayName")[0]
                    if display_name.lower() in name.lower():
                        return True
                except FileNotFoundError:
                    continue
        except FileNotFoundError:
            continue
    return False

# ----------------------------- GUI Functions -----------------------------

def run_installer():
    """Handle software installation when the user clicks the install button."""
    log("===== Installation session started =====")
    if platform.system() != "Windows":
        log("[✖] Unsupported OS. This script runs on Windows only.")
        messagebox.showerror("Unsupported OS", "This installer only works on Windows.")
        return

    for var, sw in zip(checkbox_vars, software_data):
        if var.get():
            if is_software_installed(sw["name"]):
                log(f"{sw['name']} is already installed. Skipping...")
                continue
            install_software(sw["name"], sw["installer_path"], sw["silent_flag"])

# ----------------------------- GUI Layout -----------------------------

# Create the main application window
root = tk.Tk()
root.title("Software Auto Installer")
root.geometry("650x520")
root.configure(bg="#f5f5f5")
root.resizable(True, True)

# Font definitions for consistent styling
title_font = ("Segoe UI", 12, "bold")
label_font = ("Segoe UI", 10)
button_font = ("Segoe UI", 10, "bold")

# Display USB mode banner if running from external drive
if is_running_from_usb():
    tk.Label(
        root,
        text="Portable mode detected (USB)",
        fg="blue",
        bg="#f5f5f5",
        font=("Segoe UI", 10, "italic")
    ).pack(pady=5)

# Main instruction label
tk.Label(
    root,
    text="Select the software to install:",
    bg="#f5f5f5",
    font=title_font
).pack(pady=10)

# Load software configuration and initialize variables
software_data = load_config()
checkbox_vars = []

# Create main container frame
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack()

# Create three columns for software selection
col1 = tk.Frame(frame, bg="#f5f5f5")
col2 = tk.Frame(frame, bg="#f5f5f5")
col3 = tk.Frame(frame, bg="#f5f5f5")

col1.pack(side="left", padx=15)
col2.pack(side="left", padx=15)
col3.pack(side="left", padx=15)

# Distribute 9 software items across 3 columns (3 per column)
columns = [col1, col2, col3]
for i, s in enumerate(software_data):
    var = tk.BooleanVar()
    target_col = columns[i // 3]  # 0–2 goes to col1, 3–5 to col2, 6–8 to col3
    cb = tk.Checkbutton(
        target_col,
        text=s["name"],
        variable=var,
        font=label_font,
        bg="#f5f5f5",
        anchor="w",
        padx=5
    )
    cb.pack(anchor='w', pady=2)
    checkbox_vars.append(var)

# Updater button
tk.Button(
    root,
    text="Update Installers",
    command=update_installers_from_gui,
    bg="#008CBA",
    fg="white",
    font=button_font,
    padx=10,
    pady=5
).pack(pady=(5, 0))

# Install button
tk.Button(
    root,
    text="Install Selected",
    command=run_installer,
    bg="#480DDC",
    fg="white",
    font=button_font,
    padx=12,
    pady=6
).pack(pady=15)

# Log label and scrolling output area
tk.Label(
    root,
    text="Activity Log:",
    bg="#f5f5f5",
    font=label_font
).pack()

log_area = scrolledtext.ScrolledText(
    root,
    width=80,
    height=10,
    font=("Consolas", 9)
)
log_area.pack(pady=5)
log_area.config(state="disabled")

# Start the GUI
root.mainloop()
