# This Is Notes Repository
### To Save Code, Notes, Links, And More

- [event-list-custom-html-block-workspace-frappe.md](event-list-custom-html-block-workspace-frappe.md)




    <h1>List of Markdown Files in GitHub Repository</h1>
    <div>
        <label for="user">GitHub User:</label>
        <input type="text" id="user" placeholder="Enter GitHub User" value="octocat">
    </div>
    <div>
        <label for="repo">Repository Name:</label>
        <input type="text" id="repo" placeholder="Enter Repository Name" value="Hello-World">
    </div>
    <div>
        <label for="branch">Branch:</label>
        <input type="text" id="branch" placeholder="Enter Branch Name" value="main">
    </div>

    <button id="load-files">Load Markdown Files</button>

    <ul id="file-list">
        <!-- List of markdown files will appear here -->
    </ul>

    <script>
        document.getElementById('load-files').addEventListener('click', function() {
            const user = document.getElementById('user').value;
            const repo = document.getElementById('repo').value;
            const branch = document.getElementById('branch').value;

            fetch(`https://api.github.com/repos/${user}/${repo}/git/trees/${branch}?recursive=1`)
                .then(response => response.json())
                .then(data => {
                    const files = data.tree.filter(item => item.path.endsWith('.md'));
                    const fileListElement = document.getElementById('file-list');
                    fileListElement.innerHTML = ''; // Clear previous results

                    if (files.length > 0) {
                        files.forEach(file => {
                            const listItem = document.createElement('li');
                            listItem.textContent = file.path;
                            fileListElement.appendChild(listItem);
                        });
                    } else {
                        fileListElement.innerHTML = '<li>No markdown files found.</li>';
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        });
    </script>



