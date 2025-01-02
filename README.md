# This Is Notes Repository
### To Save Code, Notes, Links, And More

- [event-list-custom-html-block-workspace-frappe.md](event-list-custom-html-block-workspace-frappe.md)


   # Project Documentation

This file is dynamically generated and lists all markdown files in the repository.

## Current Repository Information
- **User**: `{{user}}`
- **Repository**: `{{repository}}`
- **Branch**: `{{branch}}`

## List of All Markdown Files

```python
import requests

# Get the repository details (user, repository, branch)
user = "your-github-username"
repository = "your-repository-name"
branch = "main"  # or any other branch you want

# API URL to fetch the repository contents
api_url = f"https://api.github.com/repos/{user}/{repository}/contents/?ref={branch}"

# Get all files from the repository
response = requests.get(api_url)
files = response.json()

# Filter markdown files
md_files = [file['name'] for file in files if file['name'].endswith('.md')]

# Create the markdown content for the README file
markdown_content = "# List of Markdown Files in the Repository\n\n"
markdown_content += "| File Name | Link |\n"
markdown_content += "| --- | --- |\n"
for file in md_files:
    file_url = f"https://github.com/{user}/{repository}/blob/{branch}/{file}"
    markdown_content += f"| {file} | [{file}]({file_url}) |\n"

# Write the generated markdown content into a new README.md
with open('README.md', 'w') as f:
    f.write(markdown_content)
