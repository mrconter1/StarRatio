import requests
import json
import subprocess
import tempfile
import os

def count_lines_of_code(repo_dir):
    """
    Counts the lines of code in all code files in the given directory and its subdirectories.
    """
    total_lines = 0
    for root, _, files in os.walk(repo_dir):
        for file in files:
            if file.endswith(('.py', '.java', '.js', '.cpp', '.c', '.cs', '.go', '.rb', '.php', '.ts', '.swift', '.rs')):  # Add more extensions as needed
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    total_lines += sum(1 for _ in f)
    return total_lines

def clone_repo(repo_url, temp_dir):
    """
    Clones a given repository into the specified temporary directory
    and returns the path to the cloned repository.
    """
    try:
        # Construct the clone command with shallow clone option
        clone_command = f"git clone --depth 1 {repo_url} {temp_dir}"
        # Execute the clone command
        subprocess.run(clone_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
                loc_count = count_lines_of_code(clone_path)

                if loc_count > 0:
                    print(f"Cloned {repo} into {clone_path} with {loc_count} lines of code")
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
num_of_repos_to_fetch = 50

# Example usage
repos = fetch_github_repos(star_filter, num_of_repos_to_fetch)
print(repos)
print(len(repos))

# Process the repositories
repo_loc_counts = process_repos(repos)