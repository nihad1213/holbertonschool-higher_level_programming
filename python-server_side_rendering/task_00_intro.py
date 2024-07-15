import os

def generate_invitations(template_content, attendees):
    # Check if template is a string
    if not isinstance(template_content, str):
        return 'Template is not a string'
    
    # Check if template content is empty
    if not template_content.strip():
        return 'Template file is empty'
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        return 'Attendees need to be a list of dictionaries'
    
    if not attendees:
        return 'No attendees provided'

    # Generate invitation files for each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders in the template with attendee data
        invitation = template_content
        invitation = invitation.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A"))
        invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))
        
        # Write to an output file
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)
        
        print(f"Generated {output_filename}")

if __name__ == "__main__":
    # Assuming attendees list is defined here
    attendees = [
        {"name": "John Doe", "event_title": "Conference", "event_date": "2024-07-15", "event_location": "New York"},
        {"name": "Jane Smith", "event_title": "Seminar", "event_date": "2024-07-16", "event_location": "Los Angeles"}
    ]

    # Rest of your code remains the same
    template_file = "template.txt"
    if not os.path.exists(template_file):
        print('Template file does not exist')
        exit(1)

    if os.path.getsize(template_file) == 0:
        print('Template file is empty')
        exit(1)

    with open(template_file, 'r') as file:
        template_content = file.read()

    # Call the function with the template content and attendees list
    result = generate_invitations(template_content, attendees)
    if result is not None:
        print(result)
