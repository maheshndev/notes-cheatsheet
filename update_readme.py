import os

def generate_markdown_list():
    # Get all .md files in the repository
    md_files = [f for f in os.listdir() if f.endswith('.md') and f != 'README.md']
    
    # Prepare the list for the README.md
    md_list = "\n".join([f"- [{f}]({f})" for f in md_files])

    return md_list

def update_readme(md_list):
    # Open the README.md file and add the list of .md files
    with open('README.md', 'r') as file:
        readme_content = file.read()

    # Find the section where you want to insert the list, or create a new section
    section_title = "## List of Markdown Files"
    new_content = f"{section_title}\n\n{md_list}\n\n"

    # Check if the section exists already
    if section_title not in readme_content:
        # If not, append it to the end of the README.md file
        readme_content += "\n" + new_content
    else:
        # If it exists, replace the section
        readme_content = readme_content.replace(readme_content.split(section_title)[1], new_content)

    # Write the updated content back to README.md
    with open('README.md', 'w') as file:
        file.write(readme_content)

if __name__ == "__main__":
    md_list = generate_markdown_list()
    update_readme(md_list)
