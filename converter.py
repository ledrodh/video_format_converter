import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def select_file():
    file = filedialog.askopenfilename(filetypes=[("Videos", "*.mp4;*.mkv;*.avi;*.mov;*.wmv;*.flv;*.webm;*.3gp")])
    if file:
        input_var.set(file)

def convert_video():
    input_file = input_var.get()
    format_selected = format_var.get()
    
    if not input_file:
        messagebox.showerror("Error", "Please select a video file.")
        return
    
    if not format_selected:
        messagebox.showerror("Error", "Please choose an output format.")
        return
    
    output_file = input_file.rsplit(".", 1)[0] + f".{format_selected}"
    
    command = ["ffmpeg", "-i", input_file, "-c:v", "libx264", "-preset", "fast", "-c:a", "aac", "-b:a", "128k", output_file]
    
    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Conversion completed!\nSaved as {output_file}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Video conversion failed.")

# Creating the main window
window = tk.Tk()
window.title("Video Converter")
window.geometry("400x250")

# Variables
input_var = tk.StringVar()
supported_formats = ["mp4", "mkv", "avi", "mov", "wmv", "flv", "webm", "3gp"]
format_var = tk.StringVar(value=supported_formats[0])

# Widgets
tk.Label(window, text="Select the video file:").pack(pady=5)
tk.Entry(window, textvariable=input_var, width=50, state="readonly").pack(pady=5)
tk.Button(window, text="Choose File", command=select_file).pack(pady=5)

tk.Label(window, text="Choose the output format:").pack(pady=5)
tk.OptionMenu(window, format_var, *supported_formats).pack(pady=5)

tk.Button(window, text="Convert", command=convert_video).pack(pady=20)

# Run the interface
window.mainloop()
