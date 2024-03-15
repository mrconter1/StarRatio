import requests
import json

# Global variables for the number of stars and page number
NUMBER_OF_STARS = 200
PAGE_NUMBER = 1

def fetch_github_names(stars, page):
    url = f"https://github.com/search?q=stars%3A{stars}&type=repositories&p={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON content
        json_data = json.loads(response.text)
        
        # Navigate to the 'payload' and then 'results' part of the JSON
        if 'payload' in json_data and 'results' in json_data['payload']:
            # Extract 'hl_name' strings from each item in 'results'
            hl_names = [item['hl_name'] for item in json_data['payload']['results']]
        else:
            hl_names = []
        
        return hl_names
    else:
        return "Failed to fetch page"

# Example usage
hl_names = fetch_github_names(NUMBER_OF_STARS, PAGE_NUMBER)
print(hl_names)
