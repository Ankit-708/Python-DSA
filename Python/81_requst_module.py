# we use this get request to get th text of any url that we will prove here
# get request

import requests
r = requests.get("url of any site")
print(r.text) # it will print the text of the given url 
print(r.status_code) # to know the status of server like 200,201,401,etc

# post request
# it is more secure toh get method

# url = "WWw.something.com"
# data = {
#     "pi":4,
#     "p2":8
# }
# r2 = requests.post(url = url, data = data)

