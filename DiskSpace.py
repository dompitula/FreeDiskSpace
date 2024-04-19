import tkinter as tk
from tkinter import ttk
import psutil

# Function to get remaining disk space in GB
def get_disk_space():
  disk_usage = psutil.disk_usage("C:")
  disk_free = round(disk_usage.free / (1024**3), 2)
  disk_size = disk_usage.total / (2**30)
  return (disk_free, disk_size) # Convert to GB with 2 decimal places

# Function to update progress bar
def update_progress_bar():
  disk_free = get_disk_space()[0]
  disk_size = get_disk_space()[1]
  print("current size changed to: {0}".format(disk_free))
  percentage_remaining = (disk_free / disk_size) * 100
  progress_bar["value"] = int(percentage_remaining)  # Set progress bar value
  disk_space_label.config = tk.Label(window, text="Remaining Disk Space: {:.2f} GB / {:.2f} GB"
                            .format(get_disk_space()[0], get_disk_space()[1]))

# Function to restart PC (requires admin privileges)
def restart_pc():
  print("Restarting... (not)")
  # Implement logic to prompt for confirmation and restart using libraries like psutil or os (careful with restarts)

# Create the main window
window = tk.Tk()
window.title("FreeSpace Manager")
window.geometry('300x150')

# Title
disk_space_label = tk.Label(window, text="Remaining Disk Space: {:.2f} GB / {:.2f} GB"
                            .format(get_disk_space()[0], get_disk_space()[1]))
disk_space_label.pack()

# Progress bar
progress_bar = ttk.Progressbar(window, orient=tk.HORIZONTAL, mode='determinate', maximum=100)
progress_bar.pack(fill=tk.X, pady=20)  # Fill entire width and expand

# Update progress bar on window creation and call it periodically (e.g., every second)
update_progress_bar()
window.after(1000, update_progress_bar)  # Call update function every second

# Restart button
restart_button = tk.Button(window, text="Restart PC", command=restart_pc)
restart_button.pack()

# Run the main event loop
window.mainloop()