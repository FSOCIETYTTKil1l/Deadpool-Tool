import subprocess
import sys

# HIER kannst du beliebig viele Pakete eintragen
PACKAGES = [
    "pystyle",
    "requests",
    "numpy",
    "pillow",
    "flask",
    "scapy",
    "colorama",
    "rich",
    "pycryptodome",
    "beautifulsoup4"
]

def install(package):
    print(f"[INSTALL] {package} ...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
        print(f"[OK] {package} installiert.\n")
    except subprocess.CalledProcessError:
        print(f"[FEHLER] {package} konnte nicht installiert werden!\n")

def main():
    print("=== PYTHON UNIVERSAL INSTALLER ===\n")
    for pkg in PACKAGES:
        install(pkg)
    print("=== FERTIG ===")

if __name__ == "__main__":
    main()
