# Stereo to Mono Converter

A Python tool for converting multiple audio files from stereo to mono. The program supports MP3, WAV, and AIFF files and creates a ZIP file with all converted mono files.

## Features

- Converts multiple audio files simultaneously
- Supports MP3, WAV, AIFF, and AIF formats
- Recursive folder search
- Creates ZIP file with all converted files
- Terminal-based user interface
- Real-time progress bar with visual indicators
- Comprehensive error handling and validation

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

# Keep temporary files (for debugging)
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

- **Input:** MP3, WAV, AIFF, AIF
- **Output:** Same format as input (with "_mono" suffix)

## Technical Details

- **Stereo to Mono:** Average of both channels
- **Quality:** Lossless conversion (except MP3)
- **Memory:** Temporary files are automatically deleted
- **Performance:** Parallel processing possible
- **Progress Tracking:** Real-time progress bar with ETA calculation

## Error Handling

The program handles various error cases:
- Unsupported file formats
- Corrupted audio files
- Missing permissions
- Storage space issues

## License

MIT License - see LICENSE file for details.

## Contributing

Pull requests are welcome! Please create an issue for major changes.

## Support

For problems or questions, please create a GitHub issue.
