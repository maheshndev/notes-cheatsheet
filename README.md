# This Is Notes Repository
### To Save Code, Notes, Links, And More

- [event-list-custom-html-block-workspace-frappe.md](event-list-custom-html-block-workspace-frappe.md)

// GitHub API URL to list files in a repository
const repoOwner = 'your-username'; // Replace with the repository owner's username
const repoName = 'your-repo'; // Replace with the repository name
const apiUrl = `https://api.github.com/repos/${repoOwner}/${repoName}/contents/`;

// Fetch the contents of the repository
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const markdownFiles = data.filter(file => file.name.endsWith('.md')); // Filter only .md files
    const markdownLinks = markdownFiles.map(file => {
      return `<a href="${file.download_url}" target="_blank">${file.name}</a>`; // Create <a> tags for each markdown file
    });

    // Create and append the links dynamically
    const readmeLinkSection = document.getElementById('readme-links'); // Make sure you have a div with this ID in your HTML
    markdownLinks.forEach(link => {
      const listItem = document.createElement('li');
      listItem.innerHTML = link;
      readmeLinkSection.appendChild(listItem);
    });
  })
  .catch(error => console.error('Error fetching data from GitHub API:', error));
<ul id="readme-links"></ul>
