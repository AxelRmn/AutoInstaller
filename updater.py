import requests, os

def download_file(name, url, save_path):
    response = requests.get(url, stream=True)
    file_path = os.path.join(save_path, f"{name}.exe")
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print(f"Downloaded latest {name} to {file_path}")
    
if __name__ == "__main__":
    software = {
        "Chrome": "https://dl.google.com/chrome/install/latest/chrome_installer.exe",
        "VLC": "https://get.videolan.org/vlc/last/win64/vlc-setup.exe"
    }

for name, url in software.items():
    download_file(name, url, "installers")
    