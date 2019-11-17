
class Event:
    def __init__(self):
        self.date = None
        self.title = ''
        self.organizer = ''
        self.time = ''
        self.attendance = list()
        self.category = ''
        self.location = ''

    def initialize_all(self, date, title, organizer, time, category, location):
        self.date = date
        self.title = title
        self.organizer = organizer
        self.time = time
        self.category = category
        self.location = location

    def update_attendance(self, attendee):
        self.attendance.append(attendee)

class Calendar:
    def __init__(self):
        self.events = dict()
        self.category = list()

    def add_event(self, event_info):
        event = Event()
        event.initialize_all(event_info['date'], event_info['title'], event_info['organizer'], event_info['time'], event_info['category'], event_info['location'])
        self.events[event_info['title']] = event

    def get_event(self, name):
        event = self.events[name]
        event_dict = dict()
        event_dict['date'] = event.date
        event_dict['title'] = event.title
        event_dict['organizer'] = event.organizer
        event_dict['time'] = event.time
        event_dict['attendance'] = event.attendance
        event_dict['category'] = event.category
        event_dict['location'] = event.location
        return event_dict

    def filter_event(self, category):
        event_list = list()
        for key, value in self.events.iteritems():
            if value.category == category:
                event_list.append(self.get_event(key))
        return event_list
