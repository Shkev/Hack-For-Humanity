from event_classes import Event, Calendar
import datetime as dt

event = Event()
title = "Awesome Event"
organizer = "Shayan"
date_total = dt.datetime(2019, 5, 17, hour=9)
date = "%d, %d, %d" % (date_total.month, date_total.day, date_total.year)
time = "%d:%d0:%d0" % (date_total.hour, date_total.minute, date_total.second)
attendee = 'Adi'
category = 'dance'
location = 'home'
event_info = {"title":title, "organizer":organizer, "date":date, "time":time, "category":category, "location":location}

event_calendar = Calendar()
event_calendar.add_event(event_info)
event_calendar.events[title].update_attendance(attendee)
x = event_calendar.get_event(title)
print(x)
y = event_calendar.filter_event(category)
print(y)
