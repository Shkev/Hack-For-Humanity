class Resources:
    def __init__(self):
        self.title = ''
        self.content_link = ''
        self.image_link = ''
        self.host = ''
        self.location = ''
        self.category = ''
    def initialize_all(self, title, content_link, image_link, host, location, category):
        self.title = title
        self.content_link = content_link
        self.image_link = image_link
        self.host = host
        self.location = location
        self.category = category

class Menu:
    def __init__(self):
        self.resources = dict()
        self.category = list()
    def add_resource(self, resource_info):
        resource = Resources()
        resource.initialize_all(resource_info['title'], resource_info['content_link'], resource_info['image_link'], resource_info['host'], resource_info['location'], resource_info['category'])
        self.resources[resource_info['title']] = resource
    def get_resource(self, title):
        resource = self.resources[title]
        resource_dict = dict()
        resource_dict['context_link'] = resource.content_link
        resource_dict['image_link'] = resource.image_link
        resource_dict['host'] = resource.host
        resource_dict['location'] = resource.location
        resource_dict['category'] = resource.category
        return resource_dict
    def filter_resource(self, category):
        resource_list = list()
        for key, value in self.resources.iteritems():
            if value.category == category:
                resource_list.append(self.get_resource(key))
            return resource_list
