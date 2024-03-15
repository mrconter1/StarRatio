import requests
import json
import subprocess
import tempfile

def clone_repo(repo_url, temp_dir):
    """
    Clones a given repository into the specified temporary directory
    and returns the path to the cloned repository.
    """
    try:
        # Construct the clone command with shallow clone option
        clone_command = f"git clone --depth 1 {repo_url} {temp_dir}"
        # Execute the clone command
        subprocess.run(clone_command, shell=True, check=True)
        return temp_dir
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {repo_url}: {e}")
        return None

def process_repos(repos):
    """
    For each repository in the repos list, clones it into a temporary directory.
    """
    results = {}
    for repo in repos:
        # Construct the full GitHub URL for the repository
        repo_url = f"https://github.com/{repo}"

        # Create a temporary directory for the repository
        with tempfile.TemporaryDirectory() as temp_dir:
            clone_path = clone_repo(repo_url, temp_dir)
            if clone_path:
                # Here you would add the logic to count LOC in the cloned repository
                # For demonstration, we'll just print the path to the cloned repo
                print(f"Cloned {repo} into {clone_path}")
                # Placeholder for LOC counting logic
                loc_count = 0  # Replace this with actual LOC counting logic
                
                results[repo] = loc_count

    return results

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

# Process the repositories
repo_loc_counts = process_repos(repos)