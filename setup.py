from cx_Freeze import setup, Executable

# Define the executable information
target = Executable(
    script="FreeSpace.py",
    base="Win32GUI",
    icon="FreeSpace.ico"
    )

# Create the setup object
setup(
    name="FreeSpace Manager",
    version="2.1",
    description="This program helps you monitor your disk space and provides options to restart your PC or delete temporary files.",
    executables = [target]
)