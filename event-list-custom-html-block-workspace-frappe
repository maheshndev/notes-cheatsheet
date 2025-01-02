## List Employees Who Have Birthday Today 
### HTML Code 
```
<div id="birthday-list">
    <h3>Today's Birthdays</h3>
    <div id="employees"></div>
</div>
```
### JavaScript Code 
```
frappe.call({
    method: "frappe.client.get_list",
    args: {
        doctype: "Employee",
        fields: ["employee_name", "date_of_birth"]
    },
    callback(r) {
        if (r.message) {
            const today = frappe.datetime.now_date();
            const todayMonthDay = today.slice(5); // Get MM-DD format
            const employeeList = r.message.filter(employee => {
                const dob = employee.date_of_birth;
                return dob && dob.slice(5) === todayMonthDay;
            });

            if (employeeList.length > 0) {
                let employeeHtml = '';
                let i=0;
                employeeList.forEach(employee => {
                    i+=1;
                    employeeHtml += `<div class="employee">
                                        <span>${i}. </span><span>${employee.employee_name}</span>
                                     </div>`;
                });
                root_element.querySelector('#employees').innerHTML = employeeHtml;
            } else {
                root_element.querySelector('#employees').innerHTML = '<div>No birthdays today!</div>';
            }
        }
    }
});

```
### CSS Code 

```
#birthday-list {
    background-color: #f9f9f9;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#birthday-list h3 {
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
