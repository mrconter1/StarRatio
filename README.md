# StarRatio

This Python script automates the process of fetching popular GitHub repositories, cloning them, and analyzing their codebase to count the lines of code. It's a useful tool for developers and researchers interested in studying trends in repository sizes and programming languages across popular GitHub projects.

## Features

- Fetches popular GitHub repositories based on a star count filter
- Clones repositories into temporary directories
- Counts lines of code across multiple programming languages
- Handles large numbers of repositories efficiently

## Requirements

- Python 3.x
- `requests` library
- Git (command-line tool)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/github-repo-analyzer.git
   cd github-repo-analyzer
   ```

2. Install the required Python library:
   ```
   pip install requests
   ```

3. Ensure you have Git installed and accessible from the command line.

## Usage

1. Set the desired parameters in the script:
   - `star_filter`: Minimum number of stars for repositories to analyze
   - `num_of_repos_to_fetch`: Number of repositories to fetch and analyze

2. Run the script:
   ```
   python github_repo_analyzer.py
   ```

3. The script will output the list of fetched repositories and their respective line counts.

## How it Works

1. **Fetching Repositories**: The `fetch_github_repos` function uses GitHub's search API to find repositories with a specified minimum number of stars.

2. **Cloning Repositories**: Each repository is cloned into a temporary directory using a shallow clone to save time and space.

3. **Counting Lines of Code**: The script walks through each cloned repository, counting lines of code in files with specified extensions (.py, .java, .js, etc.).

4. **Results**: The script outputs the repository names and their respective line counts.

## Customization

- Modify the `count_lines_of_code` function to include or exclude specific file extensions.
- Adjust the `star_filter` and `num_of_repos_to_fetch` variables to change the criteria for repository selection.

## Limitations

- The script uses GitHub's public search API, which may have rate limits.
- Large repositories may take significant time to clone and analyze.
- The line count includes all lines in the files, including comments and blank lines.

## Contributing

Contributions to improve the GitHub Repository Analyzer are welcome. Please feel free to submit pull requests or open issues to suggest enhancements or report bugs.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy analyzing! 📊🐙
