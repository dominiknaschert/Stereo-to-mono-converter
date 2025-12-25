# Stereo to Mono Converter

A Python tool for converting multiple audio files from stereo to mono. The tool was created to quickly convert whole sample libraries to mono for devices like the Erica Synths Sample Drum or other mono compatible sample players.
The program supports MP3, WAV, and AIFF files and creates a ZIP file with all converted mono files.

## Features

- Converts multiple audio files simultaneously
- Supports MP3, WAV and AIFF formats
- Recursive folder search
- Creates ZIP file with all converted files
- Terminal-based user interface

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Stereo-to-mono-converter.git
   cd Stereo-to-mono-converter
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
# Convert individual files
python stereo_to_mono.py file1.wav file2.mp3

# Convert all files in a folder
python stereo_to_mono.py /path/to/audio/folder/

# Work with wildcards
python stereo_to_mono.py *.wav *.mp3
```

### Advanced Options

```bash
# Name the output ZIP file
python stereo_to_mono.py file1.wav file2.mp3 -o my_mono_files.zip

# Keep temporary files 
python stereo_to_mono.py file1.wav --keep-temp

# Enable verbose output
python stereo_to_mono.py file1.wav -v
```

### Show Help

```bash
python stereo_to_mono.py --help
```

## Examples

### Example 1: Individual Files
```bash
python stereo_to_mono.py song1.wav song2.mp3 song3.aiff
```
Result: `mono_converted.zip` with `song1_mono.wav`, `song2_mono.mp3`, `song3_mono.aiff`

### Example 2: Process Folder
```bash
python stereo_to_mono.py /Users/username/Music/MyAlbum/
```
Processes all audio files in the folder and subfolders recursively.

### Example 3: Custom Output
```bash
python stereo_to_mono.py *.wav -o album_mono.zip
```
Creates `album_mono.zip` with all converted WAV files.

## Supported Formats

- **Input:** MP3, WAV, AIFF
- **Output:** Same format as input (with "_mono" suffix)

## License

MIT License - see LICENSE file for details.
