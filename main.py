import requests

# Global variables for the number of stars and page number
NUMBER_OF_STARS = 200
PAGE_NUMBER = 1

def fetch_github_html(stars, page):
    # Construct the search URL based on the number of stars and page number
    url = f"https://github.com/search?q=stars%3A{stars}&type=repositories&p={page}"
    
    # Use the requests library to fetch the content of the page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch page"

# Example usage
html_content = fetch_github_html(NUMBER_OF_STARS, PAGE_NUMBER)
print(html_content)