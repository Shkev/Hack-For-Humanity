from resources import Resources
from resources import Menu
resource = Resources()
menu = Menu()
title = 'Event!'
content_link = 'https://www.research.va.gov/currents/0719-VA-aims-to-expand-artificial-intelligence-research.cfm'
image_link = 'https://www.research.va.gov/images/research-currents/july19/GilAlterovitz.jpg'
host = 'Gil Alterovitz'
location = 'San Diego'
category = 'AI'
#r_dict = dict()
#r_dict["title"] = title
#r_dict["content_link"] = content_link
#r_dict["image_link"] = image_link
#r_dict["host"] = host
#r_dict["location"] = location
#r_dict["category"] = category
r_dict = {'title':title, 'content_link':content_link, 'image_link':image_link, 'host':host, 'location':location, 'category':category}
#resource.initialize_all(title, content_link, image_link, host, location, category)
menu.add_resource(r_dict)
menu.get_resource(title)
x = menu.filter_resource(category)
print(x)
