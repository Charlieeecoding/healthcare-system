import requests
import json

def fetch_data():
    """Fetch data from a public API and print it out"""
    # Using JSONPlaceholder - a free public API for testing
    url = f'https://api.fda.gov/drug/label.json?limit=2'
    
    try:
        # Make the API request
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("✓ API request successful!")
            print(f"Status Code: {response.status_code}\n")
            
            # Parse and print the JSON data
            data = response.json()
            print("Fetched Data:")
            print(json.dumps(data, indent=2))
        else:
            print(f"✗ Error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Request failed: {e}")

if __name__ == "__main__":
    fetch_data()
