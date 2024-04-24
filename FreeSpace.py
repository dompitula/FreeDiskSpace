import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psutil
import subprocess
import os

# Function to get remaining disk space in GB
def get_disk_space():
  disk_usage = psutil.disk_usage("C:")
  disk_free = round(disk_usage.free / (1024**3), 2)
  return disk_free

# Function to update progress bar and usage value
def update_progress_bar():
  remaining_space = get_disk_space()
  total_space = psutil.disk_usage("C:").total / (1024**3)
  percentage_remaining = (remaining_space / total_space) * 100
  progress_bar["value"] = int(percentage_remaining)

  if percentage_remaining <= 5:
    progress_bar["style"] = "red.Horizontal.TProgressbar"
  elif percentage_remaining <= 10:
    progress_bar["style"] = "orange.Horizontal.TProgressbar"
  else:
    progress_bar["style"] = "green.Horizontal.TProgressbar"

  disk_space_label.config(text="Remaining Disk Space: {:.2f} GB / {:.2f} GB"
                            .format(remaining_space, total_space))

# Function to restart PC
def restart_pc():
  if messagebox.askquestion("Restart Confirmation", "Are you sure you want to restart now?") == "yes":
    subprocess.call(["shutdown", "/r", "/t", "0"])
  else:
    print("Restart cancelled.")

# Function to delete temporary files from PC
def delete_temp_files():
  folders = ("REDACTED", "REDACTED", "REDACTED", "REDACTED")
  if messagebox.askquestion("Delete Confirmation", "Are you sure you want to delete temporary files?") == "yes":
    for folder in folders:
      try:
        for filename in os.listdir(folder):
          file_path = os.path.join(folder, filename)
          try:
            if os.path.isfile(file_path):
              os.unlink(file_path)
          except Exception as e:
            print("Error deleting file: ",filename, e) 
        print("Temporary files deleted successfuly.")
      except Exception as e:
        print("Error deleting temporary files: ", e)

# Create the main window
window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(file="img\icon.png"))
window.title("FreeSpace Manager")
window.geometry('300x150')

# Style Config
style = ttk.Style()
style.theme_use("classic")
style.configure("green.Horizontal.TProgressbar", foreground='#66db1d', background='#66db1d')
style.configure("red.Horizontal.TProgressbar", foreground='#ff0000', background='#ff0000')
style.configure("orange.Horizontal.TProgressbar", foreground='#ffc100', background='#ffc100')

# Title
disk_space_label = tk.Label(window, text="Remaining Disk Space: {:.2f} GB / {:.2f} GB"
                            .format(get_disk_space(), (psutil.disk_usage("C:").total / (1024**3))))
disk_space_label.pack()

# Progress bar
progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL,
                                length=250,
                                mode='determinate', maximum=100,
                                style="green.Horizontal.TProgressbar")
progress_bar.pack(pady=5) 
update_progress_bar()

# Update values loop
def loop():
  update_progress_bar()
  window.after(1000, loop)
  window.update()

loop()

# Restart button
restart_button = tk.Button(window, text="Restart PC", command=restart_pc)
restart_button.pack(pady=5)

# Remove Temp files button
delete_temp_button = tk.Button(window, text="Delete Temp Files", command=delete_temp_files)
delete_temp_button.pack()

# Run the main event loop
window.mainloop()