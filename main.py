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
    echo =========================================
    """

    # Create a temporary file in the system's temporary directory
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".bat") as temp_file:
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
