def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template and list of attendees."""
    
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return

    if len(template) == 0:
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees):
        personalized_invite = template

        name = attendee.get("name")
        if name is None or name == "":
            name = "N/A"

        event_title = attendee.get("event_title")
        if event_title is None or event_title == "":
            event_title = "N/A"

        event_date = attendee.get("event_date")
        if event_date is None or event_date == "":
            event_date = "N/A"

        event_location = attendee.get("event_location")
        if event_location is None or event_location == "":
            event_location = "N/A"

        personalized_invite = personalized_invite.replace("{name}", str(name))
        personalized_invite = personalized_invite.replace("{event_title}", str(event_title))
        personalized_invite = personalized_invite.replace("{event_date}", str(event_date))
        personalized_invite = personalized_invite.replace("{event_location}", str(event_location))

        output_filename = f"output_{index + 1}.txt"

        with open(output_filename, 'w') as output_file:
            output_file.write(personalized_invite)
