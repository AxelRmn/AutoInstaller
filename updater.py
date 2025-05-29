import requests
import os

def download_file(name, url, save_path):
    """Download a file from a URL and save it in the specified path."""
    try:
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, f"{name}.exe")

        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"[✔] {name} downloaded successfully to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"[✖] Failed to download {name}: {e}")

def main():
    # Software to update with corresponding download URLs
    software = {
        "chrome_installer": "https://dl.google.com/chrome/install/latest/chrome_installer.exe",
        "vlc_installer": "https://plug-mirror.rcac.purdue.edu/vlc/vlc/3.0.21/win64/vlc-3.0.21-win64.exe",
        "firefox_installer": "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US",
        "7zip_installer": "https://www.7-zip.org/a/7z2301-x64.exe",
        "adobereaderpdf_installer": "https://get.adobe.com/es/reader/download?os=Windows+10&name=Reader+2025.001.20467+Spanish+Windows%2864Bit%29&lang=es&nativeOs=Windows+10&accepted=&declined=mss&preInstalled=&site=landing",
        "notepad_installer": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.8.1/npp.8.8.1.Installer.x64.exe"
    }

    print("=== Software Auto-Updater Started ===\n")
    for name, url in software.items():
        download_file(name, url, "installers")
    print("\n=== Update Process Completed ===")

if __name__ == "__main__":
    main()
