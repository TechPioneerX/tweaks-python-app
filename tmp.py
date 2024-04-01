import os
import tempfile

# Define the batch script content statically
batch_script = """
@echo off
echo Hello from Dynamic Batch Script
pause
"""

# Create a temporary file in the system's temporary directory
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".bat") as temp_file:
    temp_file.write(batch_script)
    temp_file_path = temp_file.name

# Close the temporary file
temp_file.close()

# Execute the batch script using os.system() with the correct path
os.system('"%s"' % temp_file_path)

# Wait for user input before closing the console window
input("Press Enter to exit...")

# Remove the temporary file
os.remove(temp_file_path)
