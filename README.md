# This Is Notes Repository
### To Save Code, Notes, Links, And More

- [event-list-custom-html-block-workspace-frappe.md](event-list-custom-html-block-workspace-frappe.md)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic .md Files List</title>
    <script>
        async function fetchMarkdownFiles() {
            const repoOwner = 'your-username'; // GitHub Username or Organization
            const repoName = 'your-repository-name'; // GitHub Repository Name
            const apiUrl = `https://api.github.com/repos/${repoOwner}/${repoName}/contents/`;

            try {
                // Fetch the contents of the repository
                const response = await fetch(apiUrl);
                const data = await response.json();

                // Filter out only .md files
                const markdownFiles = data.filter(item => item.name.endsWith('.md'));

                // Generate markdown with clickable links
                let markdownContent = "# List of Markdown Files\n\n";
                markdownFiles.forEach(file => {
                    markdownContent += `- [${file.name}](https://github.com/${repoOwner}/${repoName}/blob/main/${file.path})\n`;
                });

                // Display markdown in the HTML
                document.getElementById("markdownList").textContent = markdownContent;

            } catch (error) {
                console.error("Error fetching repository contents:", error);
                document.getElementById("markdownList").textContent = "Failed to fetch files.";
            }
        }

        window.onload = fetchMarkdownFiles;
    </script>
</head>
<body>
    <h1>Markdown Files in Repository</h1>
    <pre id="markdownList">Loading...</pre>
</body>
</html>
