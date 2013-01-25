from icalendar import Calendar, Event


file_names = ['/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/school.ics', '/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/personal.ics', '/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/work.ics', '/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/travel.ics', '/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/business.ics', '/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/meeting.ics', '/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/imporant.ics']

new_cal = Calendar()
new_cal.add('prodid', '-//My calendar product//mxm.dk//')
new_cal.add('version', '2.0')

for old_file_location in file_names:
    old_cal = Calendar.from_ical(open(old_file_location,'rb').read())
    for component in old_cal.walk():
        if component.name == "VEVENT":
            new_event = component
            new_cal.add_component(new_event)

new_file_location = "/Users/kevin/Library/Jarvis/JarvisCalendar/Current_Calendars/Consolidated_Calendar.ics"
new_cal_file = open(new_file_location,"wb")
new_cal_file.write(new_cal.to_ical())
new_cal_file.close()

check_cal = Calendar.from_ical(open(new_file_location,'rb').read())
for component in check_cal.walk():
    if component.name == "VEVENT":
        print(component.get("summary"))
