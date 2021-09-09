# this is essentially a workspace to get concepts going

# for example, a first hello world message
message = "Hello World"
print(message)

# or a first api call
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# or working with dictionaries in a list in a dictionary to get some sort of output from that mess
course = { 
    [{
        'id': '001', 
        'name': 'course example 1',
        'description': 'longer description of course here',
        'url': 'https://insert.url.here',
        'time_estimate': 30,
        'keywords': 'these are key words here',
        'created': '2021-09-02somethingsomething', 
        'modified': 'time:here'
    },
    {
         'id': '010', 
        'name': 'course example 2',
        'description': 'longer description of course here',
        'url': 'https://insert.another.here',
        'time_estimate': 60,
        'keywords': 'these are key words here',
        'created': '2021-09-01somethingsomething', 
        'modified': 'time:here'
    }]
}

set = course

for x, y in dctnry.items():
    print(x, y)

# turns out you have to from pprint import pprint and use that... 