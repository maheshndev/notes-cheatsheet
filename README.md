# This Is Notes Repository
### To Save Code, Notes, Links, And More

- [event-list-custom-html-block-workspace-frappe.md](event-list-custom-html-block-workspace-frappe.md)


    <h1>Generate README for GitHub Repository</h1>

    <div>
        <label for="user">GitHub Username:</label>
        <input type="text" id="user" placeholder="Enter your GitHub username">
    </div>

    <div>
        <label for="repo">Repository Name:</label>
        <input type="text" id="repo" placeholder="Enter your repository name">
    </div>

    <div>
        <label for="branch">Branch Name:</label>
        <input type="text" id="branch" placeholder="Enter branch name" value="main">
    </div>

    <button onclick="generateReadme()">Generate README</button>

    <div id="result"></div>

    <script>
        async function generateReadme() {
            const user = document.getElementById('user').value;
            const repo = document.getElementById('repo').value;
            const branch = document.getElementById('branch').value;

            if (!user || !repo || !branch) {
                alert('Please enter all the required fields!');
                return;
            }

            // GitHub API URL to get the file tree from a specific branch
            const apiUrl = `https://api.github.com/repos/${user}/${repo}/git/trees/${branch}?recursive=1`;

            try {
                // Fetch data from GitHub API
                const response = await fetch(apiUrl);
                const data = await response.json();

                if (data.message) {
                    alert('Error fetching repository data: ' + data.message);
                    return;
                }

                // Filter .md files
                const mdFiles = data.tree.filter(file => file.path.endsWith('.md'));

                if (mdFiles.length === 0) {
                    alert('No .md files found in this repository!');
                    return;
                }

                // Create README.md content
                let readmeContent = '# List of Markdown Files\n\n';
                mdFiles.forEach(file => {
                    readmeContent += `- [${file.path}](${file.url})\n`;
                });

                // Display the generated README content
                document.getElementById('result').textContent = readmeContent;

                // Optionally, you can create a downloadable README file here:
                const blob = new Blob([readmeContent], { type: 'text/markdown' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'README.md';
                link.textContent = 'Download README.md';
                document.getElementById('result').appendChild(link);

            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while fetching data from GitHub.');
            }
        }
    </script>

