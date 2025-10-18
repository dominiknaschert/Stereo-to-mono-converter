#!/usr/bin/env python3
"""
Setup-Skript für Stereo to Mono Converter
"""

import subprocess
import sys
import os

def install_requirements():
    """Installiert die erforderlichen Python-Pakete"""
    print("Installiere Python-Abhängigkeiten...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Alle Abhängigkeiten erfolgreich installiert!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Fehler beim Installieren der Abhängigkeiten: {e}")
        return False

def make_executable():
    """Macht das Hauptskript ausführbar"""
    script_path = "stereo_to_mono.py"
    if os.path.exists(script_path):
        try:
            os.chmod(script_path, 0o755)
            print(f"✓ {script_path} ist jetzt ausführbar!")
            return True
        except OSError as e:
            print(f"✗ Fehler beim Setzen der Ausführungsrechte: {e}")
            return False
    else:
        print(f"✗ {script_path} nicht gefunden!")
        return False

def main():
    print("=== Stereo to Mono Converter Setup ===")
    
    # Prüfe Python-Version
    if sys.version_info < (3, 7):
        print("✗ Python 3.7 oder höher ist erforderlich!")
        sys.exit(1)
    
    print(f"✓ Python {sys.version.split()[0]} erkannt")
    
    # Installiere Abhängigkeiten
    if not install_requirements():
        sys.exit(1)
    
    # Mache Skript ausführbar
    if not make_executable():
        sys.exit(1)
    
    print("\n=== Setup abgeschlossen! ===")
    print("\nVerwendung:")
    print("  python stereo_to_mono.py --help")
    print("  python stereo_to_mono.py file1.wav file2.mp3")

if __name__ == "__main__":
    main()
