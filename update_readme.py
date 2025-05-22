import os

def generate_markdown_tree(base_path='.'):
    markdown_lines = []

    for root, dirs, files in os.walk(base_path):
        # Skip hidden directories and files
        if '.git' in root or '__pycache__' in root:
            continue

        md_files = [f for f in files if f.endswith('.md') and f != 'README.md']
        if not md_files:
            continue

        relative_dir = os.path.relpath(root, base_path)
        header = f"### {relative_dir}" if relative_dir != '.' else "### Index"
        markdown_lines.append(header)

        for f in md_files:
            file_path = os.path.join(root, f)
            markdown_lines.append(f"- [{f}]({file_path})")

        markdown_lines.append("")  # Blank line after each section

    return "\n".join(markdown_lines)

def update_readme(markdown_tree):
    section_title = "## List of Markdown Files"

    with open("README.md", "r") as file:
        readme_content = file.read()

    if section_title in readme_content:
        readme_content = readme_content.split(section_title)[0].rstrip()

    updated_content = f"{readme_content}\n\n{section_title}\n\n{markdown_tree}\n"

    with open("README.md", "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    md_tree = generate_markdown_tree()
    update_readme(md_tree)
