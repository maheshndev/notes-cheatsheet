# HTML For Calendar View
```
<div id="custom-tabs">
      
    <div id="calendar-workorder"></div>
       
</div>
```
![image](https://github.com/user-attachments/assets/3e8a259a-cace-4c8c-80f4-ac8fcdcc4263)
![image](https://github.com/user-attachments/assets/c86754ee-2dc7-42e2-89f8-0afb8459d67f)

#JavaScript For Calander View 

```
const loadFullCalendar = async () => {
            const cssLink = document.createElement('link');
            cssLink.rel = 'stylesheet';
            cssLink.href = 'https://cdn.jsdelivr.net/npm/fullcalendar/main.min.css';
            document.head.appendChild(cssLink);

            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/fullcalendar/main.min.js';
            script.onload = initCalendars;
            document.head.appendChild(script);
        };

        const initCalendars = () => {
            const root = root_element.querySelector('#custom-tabs');


            const calendarWorkorder = new FullCalendar.Calendar(root_element.querySelector('#calendar-workorder'), {
                initialView: 'dayGridMonth',
                events: async () => {
                    const response = await frappe.call({
                        method: "frappe.client.get_list",
                        args: { doctype: "Work Order", fields: ["name", "planned_start_date", "planned_end_date"] }
                    });
                    return response.message.map(event => ({
                        title: event.name,
                        start: event.planned_start_date,
                        end: event.planned_end_date,
                       
                    }));
                },
                eventClick: function(info) {
                    const eventName = info.event.title;
                    // frappe.msgprint(`Event Clicked: ${eventName}`);
                     window.open(`/app/work-order/${eventName}`, "_blank");
                }
            });
            calendarWorkorder.render();

          
        };

        loadFullCalendar();
```
#CSS For Calandar View
https://cdn.jsdelivr.net/npm/fullcalendar/main.min.css
