# Stereo to Mono Converter

Ein Python-Tool zum Konvertieren mehrerer Audio-Dateien von Stereo zu Mono. Das Programm unterstützt MP3, WAV und AIFF Dateien und erstellt eine ZIP-Datei mit allen konvertierten Mono-Dateien.

## Features

- Konvertiert mehrere Audio-Dateien gleichzeitig
- Unterstützt MP3, WAV, AIFF und AIF Formate
- Rekursive Ordner-Durchsuchung
- Erstellt ZIP-Datei mit allen konvertierten Dateien
- Terminal-basierte Benutzeroberfläche
- Detaillierte Fortschrittsanzeige
- Fehlerbehandlung und Validierung

## Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/ihr-username/Stereo-to-mono-converter.git
   cd Stereo-to-mono-converter
   ```

2. **Python-Abhängigkeiten installieren:**
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

### Grundlegende Verwendung

```bash
# Einzelne Dateien konvertieren
python stereo_to_mono.py file1.wav file2.mp3

# Alle Dateien in einem Ordner konvertieren
python stereo_to_mono.py /path/to/audio/folder/

# Mit Wildcards arbeiten
python stereo_to_mono.py *.wav *.mp3
```

### Erweiterte Optionen

```bash
# Ausgabe-ZIP-Datei benennen
python stereo_to_mono.py file1.wav file2.mp3 -o my_mono_files.zip

# Temporäre Dateien behalten (für Debugging)
python stereo_to_mono.py file1.wav --keep-temp
```

### Hilfe anzeigen

```bash
python stereo_to_mono.py --help
```

## Beispiele

### Beispiel 1: Einzelne Dateien
```bash
python stereo_to_mono.py song1.wav song2.mp3 song3.aiff
```
Ergebnis: `mono_converted.zip` mit `song1_mono.wav`, `song2_mono.mp3`, `song3_mono.aiff`

### Beispiel 2: Ordner verarbeiten
```bash
python stereo_to_mono.py /Users/username/Music/MyAlbum/
```
Verarbeitet alle Audio-Dateien im Ordner und Unterordnern rekursiv.

### Beispiel 3: Benutzerdefinierte Ausgabe
```bash
python stereo_to_mono.py *.wav -o album_mono.zip
```
Erstellt `album_mono.zip` mit allen konvertierten WAV-Dateien.

## Unterstützte Formate

- **Eingabe:** MP3, WAV, AIFF, AIF
- **Ausgabe:** Gleiches Format wie Eingabe (mit "_mono" Suffix)

## Technische Details

- **Stereo zu Mono:** Durchschnitt der beiden Kanäle
- **Qualität:** Verlustfreie Konvertierung (außer MP3)
- **Speicher:** Temporäre Dateien werden automatisch gelöscht
- **Performance:** Parallele Verarbeitung möglich

## Fehlerbehandlung

Das Programm behandelt verschiedene Fehlerfälle:
- Nicht unterstützte Dateiformate
- Beschädigte Audio-Dateien
- Fehlende Berechtigungen
- Speicherplatz-Probleme

## Lizenz

MIT License - siehe LICENSE Datei für Details.

## Beitragen

Pull Requests sind willkommen! Bitte erstellen Sie ein Issue für größere Änderungen.

## Support

Bei Problemen oder Fragen erstellen Sie bitte ein GitHub Issue.
