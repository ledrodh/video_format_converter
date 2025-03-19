# Video Converter with Tkinter and FFmpeg

## Overview
This project is a **Video Converter** with a graphical user interface built using **Tkinter** and powered by **FFmpeg**. It allows users to select a video file and convert it into various formats, such as **MP4, MKV, AVI, MOV, WMV, FLV, WebM, and 3GP**. The tool provides a simple and user-friendly experience, making video format conversion easy and efficient.

## Features
- 📂 **File Selection**: Users can choose a video file through the interface.
- 🎞 **Multiple Output Formats**: Convert videos to MP4, MKV, AVI, MOV, WMV, FLV, WebM, and 3GP.
- ⚡ **Fast and Efficient**: Uses **FFmpeg** for high-quality conversions.
- ✅ **Error Handling**: Alerts users if no file is selected or if an error occurs during conversion.
- 🔹 **Simple UI**: Built with **Tkinter** for ease of use.

## Requirements
Make sure you have the following dependencies installed before running the program:

- Python 3.x
- Tkinter (comes pre-installed with Python)
- FFmpeg (must be installed on your system)

### Installing FFmpeg

#### Windows:
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
2. Extract the files and add the **bin** folder to your system's PATH.

#### macOS (Homebrew):
```sh
brew install ffmpeg
```

#### Linux (Ubuntu/Debian):
```sh
sudo apt update && sudo apt install ffmpeg
```

## Installation & Usage
1. Clone this repository:
```sh
git clone https://github.com/ledrodh/https://github.com/ledrodh/video_format_converter.git
cd video_format_converter

```
2. Run the Python script:
```sh
python video_converter.py
```

## How It Works
1. **Select a Video File**: Click the "Choose File" button.
2. **Choose Output Format**: Select a format from the dropdown menu.
3. **Convert**: Click the "Convert" button, and FFmpeg will process the conversion.
4. **Success Message**: Once the conversion is complete, a notification appears with the saved file location.

## Example Code
```python
def select_file():
    file = filedialog.askopenfilename(filetypes=[("Videos", "*.mp4;*.mkv;*.avi;*.mov;*.wmv;*.flv;*.webm;*.3gp")])
    if file:
        input_var.set(file)
```



## Author
- **ledrodh** - [GitHub](https://github.com/ledrodh)

