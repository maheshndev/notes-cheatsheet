#HTML Code
```

<div id="custom-tabs">
  <!-- Tab buttons -->
  <ul class="nav nav-tabs" id="tab-buttons" role="tablist">
    <li class="nav-item" role="presentation">
      <a class="nav-link active" id="user-tab" data-bs-toggle="tab" href="#user-tab-pane" role="tab" aria-controls="user-tab-pane" aria-selected="true">Project List</a>
    </li>
    <li class="nav-item" role="presentation">
      <a class="nav-link" id="employee-tab" data-bs-toggle="tab" href="#employee-tab-pane" role="tab" aria-controls="employee-tab-pane" aria-selected="false">Employee List</a>
    </li>
  </ul>

  <!-- Tab content -->
  <div class="tab-content" id="tab-content" style="margin-top:15px;">
    <div class="tab-pane fade show active" id="user-tab-pane" role="tabpanel" aria-labelledby="user-tab">
      
     
    <div id="bar-chart-container">
    <!--<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>-->
    <canvas id="bar-chart" width="400" height="200"></canvas>
</div>
      
      <div id="user-loader" class="text-center mt-3" style="display:none;">Loading User Data...</div>
    </div>
    <div class="tab-pane fade" id="employee-tab-pane" role="tabpanel" aria-labelledby="employee-tab">
     
     <div id="employee-chart-container">
         <!--<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>-->
        <canvas id="employee-chart" width="400" height="200"></canvas>
    </div>
      <div id="employee-loader" class="text-center mt-3" style="display:none;">Loading Employee Data...</div>
    </div>
  </div>
</div>

```
#JavaScript Code 
```
const root = root_element.getElementById('custom-tabs');

    // Tab switching
    function switchTab(tabId) {
      root.querySelectorAll('.nav-link').forEach(tab => tab.classList.remove('active'));
      root.querySelectorAll('.tab-pane').forEach(tab => tab.classList.remove('show', 'active'));

      root.querySelector(tabId).classList.add('show', 'active');
      root.querySelector([href="${tabId}"]).classList.add('active');
    }

    root.querySelectorAll('#tab-buttons .nav-link').forEach(tab => {
      tab.addEventListener('click', function(e) {
        e.preventDefault();
        switchTab(this.getAttribute('href'));
      });
    });

// Fetch projects and their custom_progress_completed values
frappe.call({
    method: "frappe.client.get_list",
    args: {
        doctype: "Project",
        fields: ["name", "percent_complete"],
        limit_page_length: 100  // Adjust as needed
    },
    callback: function(response) {
        if (response.message) {
            const projects = response.message;
            const labels = projects.map(project => project.name);
            const data = projects.map(project => project.percent_complete || 0);
             const colors = [
                '#FF6384', // Red
                '#36A2EB', // Blue
                '#FFCE56', // Yellow
                '#4BC0C0', // Teal
                '#9966FF', // Purple
                '#FF9F40'  // Orange
            ];

            // Create the bar chart
            const ctx = root_element.querySelector('#bar-chart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Progress Completed (%)',
                        data: data,
                        backgroundColor:  colors.slice(0, labels.length),
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            min: 0,
                            max: 100,
                            ticks: {
                                stepSize: 10
                            }
                        }
                    },
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        } else {
            console.error("No projects found or error fetching data.");
        }
    }
});


// Fetch Employee Status Data
frappe.call({
    method: "frappe.client.get_list",
    args: {
        doctype: "Employee",
        fields: ["status", "count(name) as count"],
        group_by: "status"
    },
    callback: function(response) {
        if (response.message) {
            const statuses = response.message.map(emp => emp.status);
            const counts = response.message.map(emp => emp.count);

            const colors = [
                '#FF6384', // Red
                '#36A2EB', // Blue
                '#FFCE56', // Yellow
                '#4BC0C0', // Teal
                '#9966FF', // Purple
                '#FF9F40'  // Orange
            ];

            const ctx = root_element.querySelector('#employee-chart').getContext('2d');
            
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: statuses,
                    datasets: [{
                        label: 'Employee Count by Status',
                        data: counts,
                        backgroundColor: colors.slice(0, statuses.length), // Limit colors to the number of statuses
                        borderColor: '#ffffff',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        }
    }
});

```
