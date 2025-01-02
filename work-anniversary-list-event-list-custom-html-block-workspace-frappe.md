## Custom HTML Block For Work Anniversary in frappe 

### HTML Code 
```
<div id="work-anniversary-list">
    <h3>Today's Work Anniversary</h3>
    <div id="employees"></div>
</div>

```
### JavaScript Code
```
frappe.call({
    method: "frappe.client.get_list",
    args: {
        doctype: "Employee",
        fields: ["employee_name", "date_of_joining"]
    },
    callback(r) {
        if (r.message) {
            const today = frappe.datetime.now_date();
            const todayMonthDay = today.slice(5); // Get MM-DD format
            const employeeList = r.message.filter(employee => {
                const doj = employee.date_of_joining;
                return doj && doj.slice(5) === todayMonthDay;
            });

            if (employeeList.length > 0) {
                let employeeHtml = '';
                let i = 0;
                employeeList.forEach(employee => {
                    i += 1;
                    employeeHtml += `<div class="employee">
                                        <span>${i}. </span><span>${employee.employee_name}</span>
                                     </div>`;
                });
                root_element.querySelector('#employees').innerHTML = employeeHtml;
            } else {
                root_element.querySelector('#employees').innerHTML = '<div>No work anniversaries today!</div>';
            }
        }
    }
});

```
### CSS Code 
```
#work-anniversary-list {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#work-anniversary-list h3 {
    margin-bottom: 10px;
    color: #333;
}

.employee {
    padding: 5px 0;
    border-bottom: 1px solid #eaeaea;
}
.employee:last-child {
    border-bottom: none;
}

```
