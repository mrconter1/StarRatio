import requests
import json

def fetch_github_repos(stars, num_of_repos):
    
    current_page = 1
    results = []
    
    while len(results) <= num_of_repos:
    
        url = f"https://github.com/search?q=stars%3A{stars}&type=repositories&p={current_page}"
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
                
            results.extend(hl_names)
            
        current_page += 1
            
    return results[:num_of_repos]

# Global variables for the number of stars and page number
star_filter = 200
num_of_repos_to_fetch = 25

# Example usage
repos = fetch_github_repos(star_filter, num_of_repos_to_fetch)
print(repos)
print(len(repos))