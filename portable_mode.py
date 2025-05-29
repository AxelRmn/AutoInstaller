import os, shutil

def is_usb_drive(path):
    return os.path.splitdrive(path)[0] != "C:"

def run_portable():
    current_drive = os.path.splitdrive(os.getcwd())[0]
    if is_usb_drive(current_drive):
        print("Running in USB mode.")
        os.makedirs("logs", exist_ok=True)
        os.makedirs("installers", exist_ok=True)
    else:
        print("Not running from USB. Limited functionality")
    
    if __name__ == "__main__":
        run_portable()
        