import json, subprocess, os, datetime, platform

def log(message):
    with open("logs/install_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")
    print(message)

def install_software(name, path, flag):
    try:
        log(f"[>] Installing {name}...")
        subprocess.run([path, flag], check=True)
        log(f"[✔] {name} installed successfully.")
    except subprocess.CalledProcessError:
        log(f"[✖] Installation failed for {name}")

def load_config():
    with open("config/software_list.json", "r") as f:
        return json.load(f)["software"]
    
if __name__ == "__main__":
    log("===== Installation session started =====")
    if platform.system() != "Windows":
        log("This script supports Windows only!")
    else:
        for s in load_config():
            install_software(s["name"], s["installer_path"], s["silent_flag"])
            