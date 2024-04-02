import os
import tempfile
import requests
import sys

# Get user input for authentication
email = input("Enter your email address: ")
api_key = input("Enter your API Key: ")

# Define the authentication endpoint
auth_url = "http://195.149.87.246:8000/api/v1/authenticate"
auth_headers = {
    "apiKey": api_key
}
auth_data = {"email": email}
auth_response = None

try:
    # Send the authentication request
    auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)
except requests.exceptions.ConnectionError:
    print("Can not connect to authentication server.")
    input("Press Enter to exit...")
    sys.exit()
except requests.exceptions.RequestException:
    print("Can not request to authentication server.")
    input("Press Enter to exit...")
    sys.exit()

# Print the whole authentication response
if auth_response is not None:
    print(auth_response.text)
else:
    print("No response received from the authentication server.")
    input("Press Enter to exit...")
    sys.exit()

# Check the authentication response
if auth_response.status_code != 200:
    print(f"{auth_response.json()['message']}")
    # Wait for user input before closing the console window
    input("Press Enter to exit...")
    sys.exit()
else:
    # Define the batch script content statically
    batch_script = """
    @echo off
    echo =========================================
    echo Hello from Dynamic Batch Script
echo. 8888888b.                   888                                 8888888b.          d8b          888    
echo. 888   Y88b                  888                                 888   Y88b         Y8P          888    
echo. 888    888                  888                                 888    888                      888    
echo. 888   d88P .d88b.  .d8888b  888888 .d88b.  888d888 .d88b.       888   d88P .d88b.  888 88888b.  888888 
echo. 8888888P" d8P  Y8b 88K      888   d88""88b 888P"  d8P  Y8b      8888888P" d88""88b 888 888 "88b 888    
echo. 888 T88b  88888888 "Y8888b. 888   888  888 888    88888888      888       888  888 888 888  888 888    
echo. 888  T88b Y8b.          X88 Y88b. Y88..88P 888    Y8b.          888       Y88..88P 888 888  888 Y88b.  
echo. 888   T88b "Y8888   88888P'  "Y888 "Y88P"  888     "Y8888       888        "Y88P"  888 888  888  "Y888 
    echo =========================================
    """

    # Create a temporary file in the system's temporary directory
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".bat", encoding='utf-8') as temp_file:
        temp_file.write(batch_script)
        temp_file_path = temp_file.name

    # Close the temporary file
    temp_file.close()

    # Execute the batch script using os.system() with the correct path
    os.system('"%s"' % temp_file_path)

    # Remove the temporary file
    os.remove(temp_file_path)

    # Wait for user input before closing the console window
    input("Press Enter to exit...")
