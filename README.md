# This Is Notes Repository
### To Save Code, Notes, Links, And More

- [event-list-custom-html-block-workspace-frappe.md](event-list-custom-html-block-workspace-frappe.md)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Markdown Files</title>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const urlParams = new URLSearchParams(window.location.search);
            const user = urlParams.get('user');
            const repo = urlParams.get('repository');
            const branch = urlParams.get('branch') || 'main'; // Default to 'main' if branch is not provided

            if (!user || !repo) {
                alert("User and repository parameters are required!");
                return;
            }

            const apiUrl = `https://api.github.com/repos/${user}/${repo}/contents?ref=${branch}`;
            
            fetch(apiUrl)
                .then(response => response.json())
                .then(data => {
                    const markdownFiles = data.filter(item => item.name.endsWith('.md'));
                    displayFiles(markdownFiles);
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });

            function displayFiles(files) {
                const filesList = document.getElementById('files-list');
                filesList.innerHTML = '';

                if (files.length === 0) {
                    filesList.innerHTML = '<li>No markdown files found.</li>';
                    return;
                }

                files.forEach(file => {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `<a href="${file.html_url}" target="_blank">${file.name}</a>`;
                    filesList.appendChild(listItem);
                });
            }
        });
    </script>
</head>
<body>
    <h1>Markdown Files in GitHub Repository</h1>
    <ul id="files-list">
        <!-- Markdown files will be listed here -->
    </ul>
</body>
</html>
