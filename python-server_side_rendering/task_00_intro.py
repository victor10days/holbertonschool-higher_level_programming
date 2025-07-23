import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated. ")
        return
    
    for i, attendee in enumerate(attendees, 1):
        content = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key) or "N/A"
            content = content.replace(f"{{{key}}}", value)
        with open(f"output_{i}.txt", "w") as file:
            file.write(content)