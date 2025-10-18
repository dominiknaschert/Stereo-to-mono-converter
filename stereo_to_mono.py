#!/usr/bin/env python3
"""
Stereo to Mono Converter
Konvertiert mehrere Audio-Dateien (MP3, WAV, AIFF) von Stereo zu Mono
und erstellt eine ZIP-Datei mit allen konvertierten Dateien.
"""

import os
import sys
import argparse
import zipfile
import tempfile
from pathlib import Path
import librosa
import soundfile as sf
import numpy as np
from typing import List, Tuple
import time

class ProgressBar:
    """Einfacher Fortschrittsbalken für das Terminal"""
    
    def __init__(self, total: int, width: int = 50):
        self.total = total
        self.width = width
        self.current = 0
        self.start_time = time.time()
    
    def update(self, current: int, item_name: str = ""):
        """Aktualisiert den Fortschrittsbalken"""
        self.current = current
        progress = current / self.total
        filled_width = int(self.width * progress)
        
        # Erstelle Fortschrittsbalken mit ||
        bar = "|" * filled_width + " " * (self.width - filled_width)
        
        # Berechne Zeit und Geschwindigkeit
        elapsed = time.time() - self.start_time
        if current > 0:
            eta = (elapsed / current) * (self.total - current)
            eta_str = f"ETA: {eta:.1f}s"
        else:
            eta_str = "ETA: --"
        
        # Zeige Fortschritt
        print(f"\r[{bar}] {current}/{self.total} ({progress*100:.1f}%) {eta_str} | {item_name[:30]:<30}", end="", flush=True)
    
    def finish(self):
        """Beendet den Fortschrittsbalken"""
        elapsed = time.time() - self.start_time
        print(f"\n✓ Alle {self.total} Dateien in {elapsed:.1f}s konvertiert!")

class StereoToMonoConverter:
    def __init__(self):
        self.supported_formats = {'.mp3', '.wav', '.aiff', '.aif'}
        
    def is_supported_file(self, file_path: str) -> bool:
        """Prüft ob die Datei ein unterstütztes Audio-Format hat"""
        return Path(file_path).suffix.lower() in self.supported_formats
    
    def convert_to_mono(self, input_path: str, output_path: str, verbose: bool = False) -> bool:
        """
        Konvertiert eine Audio-Datei von Stereo zu Mono
        
        Args:
            input_path: Pfad zur Eingabedatei
            output_path: Pfad zur Ausgabedatei
            verbose: Detaillierte Ausgabe aktivieren
            
        Returns:
            True wenn erfolgreich, False bei Fehler
        """
        try:
            if verbose:
                print(f"Konvertiere: {os.path.basename(input_path)}")
            
            # Lade Audio-Datei
            audio_data, sample_rate = librosa.load(input_path, sr=None, mono=False)
            
            # Prüfe ob die Datei Stereo ist
            if len(audio_data.shape) == 1:
                if verbose:
                    print(f"  → Datei ist bereits Mono")
                mono_audio = audio_data
            else:
                if verbose:
                    print(f"  → Konvertiere Stereo zu Mono")
                # Konvertiere Stereo zu Mono (Durchschnitt der beiden Kanäle)
                mono_audio = np.mean(audio_data, axis=0)
            
            # Speichere als Mono-Datei
            sf.write(output_path, mono_audio, sample_rate)
            if verbose:
                print(f"  ✓ Erfolgreich konvertiert")
            return True
            
        except Exception as e:
            if verbose:
                print(f"  ✗ Fehler bei der Konvertierung: {e}")
            return False
    
    def get_audio_files(self, input_paths: List[str]) -> List[str]:
        """
        Sammelt alle unterstützten Audio-Dateien aus den gegebenen Pfaden
        
        Args:
            input_paths: Liste von Datei- oder Ordnerpfaden
            
        Returns:
            Liste von Audio-Dateipfaden
        """
        audio_files = []
        
        for path in input_paths:
            path_obj = Path(path)
            
            if path_obj.is_file():
                if self.is_supported_file(path):
                    audio_files.append(str(path_obj.absolute()))
                else:
                    print(f"Warnung: {path} ist kein unterstütztes Audio-Format")
            elif path_obj.is_dir():
                # Durchsuche Ordner rekursiv nach Audio-Dateien
                for file_path in path_obj.rglob('*'):
                    if file_path.is_file() and self.is_supported_file(file_path):
                        audio_files.append(str(file_path.absolute()))
            else:
                print(f"Warnung: {path} existiert nicht")
        
        return audio_files
    
    def convert_files(self, input_paths: List[str], output_dir: str = None, verbose: bool = False) -> Tuple[List[str], List[str]]:
        """
        Konvertiert alle Audio-Dateien zu Mono
        
        Args:
            input_paths: Liste von Eingabepfaden
            output_dir: Ausgabeordner (optional)
            verbose: Detaillierte Ausgabe aktivieren
            
        Returns:
            Tuple von (erfolgreiche Konvertierungen, Fehler)
        """
        # Sammle alle Audio-Dateien
        audio_files = self.get_audio_files(input_paths)
        
        if not audio_files:
            print("Keine unterstützten Audio-Dateien gefunden!")
            return [], []
        
        print(f"\nGefundene Audio-Dateien: {len(audio_files)}")
        if verbose:
            for file in audio_files:
                print(f"  - {os.path.basename(file)}")
        
        # Erstelle temporären Ausgabeordner
        if output_dir is None:
            output_dir = tempfile.mkdtemp(prefix="mono_converted_")
        else:
            os.makedirs(output_dir, exist_ok=True)
        
        if verbose:
            print(f"\nAusgabeordner: {output_dir}")
        
        print("\nStarte Konvertierung...")
        
        # Erstelle Fortschrittsbalken
        progress_bar = ProgressBar(len(audio_files))
        
        converted_files = []
        errors = []
        
        for i, input_file in enumerate(audio_files):
            # Aktualisiere Fortschrittsbalken
            current_filename = os.path.basename(input_file)
            progress_bar.update(i, current_filename)
            
            # Erstelle Ausgabedateiname
            input_name = Path(input_file).stem
            input_ext = Path(input_file).suffix
            output_filename = f"{input_name}_mono{input_ext}"
            output_path = os.path.join(output_dir, output_filename)
            
            # Konvertiere Datei
            if self.convert_to_mono(input_file, output_path, verbose):
                converted_files.append(output_path)
            else:
                errors.append(input_file)
        
        # Beende Fortschrittsbalken
        progress_bar.finish()
        
        return converted_files, errors
    
    def create_zip(self, file_paths: List[str], zip_path: str) -> bool:
        """
        Erstellt eine ZIP-Datei mit allen konvertierten Dateien
        
        Args:
            file_paths: Liste von Dateipfaden
            zip_path: Pfad zur ZIP-Datei
            
        Returns:
            True wenn erfolgreich, False bei Fehler
        """
        try:
            print(f"\nErstelle ZIP-Datei: {zip_path}")
            
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file_path in file_paths:
                    filename = os.path.basename(file_path)
                    zipf.write(file_path, filename)
                    print(f"  ✓ Hinzugefügt: {filename}")
            
            print(f"✓ ZIP-Datei erfolgreich erstellt")
            return True
            
        except Exception as e:
            print(f"✗ Fehler beim Erstellen der ZIP-Datei: {e}")
            return False
    
    def cleanup_temp_files(self, file_paths: List[str]):
        """Löscht temporäre Dateien"""
        for file_path in file_paths:
            try:
                os.remove(file_path)
            except OSError:
                pass

def main():
    parser = argparse.ArgumentParser(
        description="Konvertiert Audio-Dateien von Stereo zu Mono und erstellt eine ZIP-Datei",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python stereo_to_mono.py file1.wav file2.mp3
  python stereo_to_mono.py /path/to/audio/folder/
  python stereo_to_mono.py *.wav -o converted.zip
  python stereo_to_mono.py file1.wav file2.mp3 -o my_mono_files.zip
        """
    )
    
    parser.add_argument(
        'input_paths',
        nargs='+',
        help='Audio-Dateien oder Ordner mit Audio-Dateien'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Name der Ausgabe-ZIP-Datei (Standard: mono_converted.zip)',
        default='mono_converted.zip'
    )
    
    parser.add_argument(
        '--keep-temp',
        action='store_true',
        help='Behalte temporäre Dateien nach der ZIP-Erstellung'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Detaillierte Ausgabe aktivieren'
    )
    
    args = parser.parse_args()
    
    # Prüfe ob Eingabepfade existieren
    for path in args.input_paths:
        if not os.path.exists(path):
            print(f"Fehler: Pfad '{path}' existiert nicht!")
            sys.exit(1)
    
    print("=== Stereo to Mono Converter ===")
    print(f"Eingabepfade: {', '.join(args.input_paths)}")
    print(f"Ausgabe-ZIP: {args.output}")
    
    # Erstelle Converter-Instanz
    converter = StereoToMonoConverter()
    
    # Konvertiere Dateien
    converted_files, errors = converter.convert_files(args.input_paths, verbose=args.verbose)
    
    if not converted_files:
        print("\n✗ Keine Dateien konnten konvertiert werden!")
        if errors:
            print("Fehler:")
            for error in errors:
                print(f"  - {error}")
        sys.exit(1)
    
    # Erstelle ZIP-Datei
    if converter.create_zip(converted_files, args.output):
        print(f"\n✓ Erfolgreich abgeschlossen!")
        print(f"ZIP-Datei erstellt: {os.path.abspath(args.output)}")
        print(f"Konvertierte Dateien: {len(converted_files)}")
        
        if errors:
            print(f"Fehlerhafte Dateien: {len(errors)}")
            for error in errors:
                print(f"  - {os.path.basename(error)}")
    else:
        print("\n✗ Fehler beim Erstellen der ZIP-Datei!")
        sys.exit(1)
    
    # Lösche temporäre Dateien falls gewünscht
    if not args.keep_temp:
        converter.cleanup_temp_files(converted_files)
        print("Temporäre Dateien gelöscht.")

if __name__ == "__main__":
    main()
