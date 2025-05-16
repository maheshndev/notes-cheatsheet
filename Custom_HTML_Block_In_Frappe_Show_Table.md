# Custom HTML Block to show table in workspace inside tabs "Work Order", "Job Card"

## HTML Code 
```
<div id="custom-tabs">
  <!-- Tab buttons -->
  <ul class="nav nav-tabs" id="tab-buttons" role="tablist">
    <li class="nav-item" role="presentation">
      <a class="nav-link active" id="user-tab" data-bs-toggle="tab" href="#user-tab-pane" role="tab" aria-controls="user-tab-pane" aria-selected="true">Work Order List</a>
    </li>
    <li class="nav-item" role="presentation">
      <a class="nav-link" id="employee-tab" data-bs-toggle="tab" href="#employee-tab-pane" role="tab" aria-controls="employee-tab-pane" aria-selected="false">Job Card List</a>
    </li>
  </ul>

  <!-- Tab content -->
  <div class="tab-content" id="tab-content" style="margin-top:15px;">
    <div class="tab-pane fade show active" id="user-tab-pane" role="tabpanel" aria-labelledby="user-tab">
      
     
     <table class="table table-bordered table-condensed" id="work_order_table"></table>
      
      <div id="user-loader" class="text-center mt-3" style="display:none;">Loading User Data...</div>
    </div>
    <div class="tab-pane fade" id="employee-tab-pane" role="tabpanel" aria-labelledby="employee-tab">
     
     <table class="table table-bordered table-condensed" id="job_card_table"></table>
      <div id="employee-loader" class="text-center mt-3" style="display:none;">Loading Employee Data...</div>
    </div>
  </div>
</div>
```
![image](https://github.com/user-attachments/assets/92ae1bd0-b9a0-4c7b-b34c-86230aeb9311)

## JavaScript Code

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
// -------------------------------------------------------------------------------------------------------------------
  frappe.call({
    method: "frappe.client.get_list",
    args: {
      doctype: "Work Order",
      filters: {
        status: ['In',["Draft","Submitted","Not Started","In Process","Completed","Stopped","Closed","Cancelled"]]
      },
      fields: ["name", "item_name", "status", "qty"],
    },
    callback: function (response) {
      if (response.message) {
        populateWorkOrderTable(response.message);
      } else {
        console.error("No task list data found.");
      }
    },
    error: function (xhr, status, error) {
      console.error("Error fetching task list:", error);
    },
  });

  function populateWorkOrderTable(tasks) {
    var workOrderTable = root_element.querySelector("#work_order_table");
    var tableHTML = "<thead>";
    tableHTML += "<thead><tr><th>Work Order ID</th><th>Item Name</th><th>Status</th><th>Qty To Manufacture</th></tr></thead>";
    tableHTML += "<tbody>";

    tasks.forEach(function (task) {
      tableHTML += "<tr>";
      tableHTML += "<td><a href='/app/work-order/" + task.name + "'>" + task.name + "</a></td>";
      tableHTML += "<td>" + task.item_name + "</td>";

      var statusColor = task.status === "In Process" ? "red" : "green";
      tableHTML += "<td style='color: " + statusColor + ";'>" + task.status + "</td>";

      
      tableHTML += "<td >" + task.qty + "</td>";

      tableHTML += "</tr>";
    });

    tableHTML += "</tbody>";

    workOrderTable.innerHTML = tableHTML;
  }
  
//   --------------------------------------------------------------------------------------------------------------------------
frappe.call({
    method: "frappe.client.get_list",
    args: {
      doctype: "Job Card",
      filters: {
        status: ['In',["Open","Work In Progress","aterial Transferred","On Hold","Submitted","Cancelled","Completed"]]
      },
      fields: ["name", "operation", "status", "for_quantity","total_completed_qty", "workstation", "work_order"],
    },
    callback: function (response) {
      if (response.message) {
        populateJobCardTable(response.message);
      } else {
        console.error("No task list data found.");
      }
    },
    error: function (xhr, status, error) {
      console.error("Error fetching task list:", error);
    },
  });

  function populateJobCardTable(tasks) {
    var jobCardTable = root_element.querySelector("#job_card_table");
    var tableHTML = "<thead>";
    tableHTML += "<thead><tr><th>Job Card ID</th><th>Operation</th><th>Status</th><th>Qty To Manufacture</th><th>Total Completed Qty</th><th>Workstation</th><th>Work Order</th></tr></thead>";
    tableHTML += "<tbody>";

    tasks.forEach(function (task) {
      tableHTML += "<tr>";
      tableHTML += "<td><a href='/app/job-card/" + task.name + "'>" + task.name + "</a></td>";
      tableHTML += "<td>" + task.operation + "</td>";

      var statusColor = "";
      switch(task.status) {
        case "Cancelled":
          statusColor = "red";
          break;
        case "Work In Progress":
          statusColor = "orange";
          break;
        case "Open":
          statusColor = "#8B8000";
          break;
        case "Completed":
          statusColor = "green";
          break;
        default:
          statusColor = "inherit";
      }
      tableHTML += "<td style='color: " + statusColor + ";'>" + task.status + "</td>";

      
      
      tableHTML += "<td >" + task.for_quantity + "</td>";
      tableHTML += "<td >" + task.total_completed_qty + "</td>";
      tableHTML += "<td >" + task.workstation + "</td>";
      tableHTML += "<td >" + task.work_order + "</td>";

      tableHTML += "</tr>";
    });

    tableHTML += "</tbody>";

    jobCardTable.innerHTML = tableHTML;
  }
```
![image](https://github.com/user-attachments/assets/a36a38d7-db72-492b-aa59-57dfa2217267)
