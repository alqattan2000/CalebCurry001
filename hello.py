import requests

print(requests.get('https://google.com').cookies)

response = requests.get('https://api.stackexchange.com/2.3/posts?order=desc&sort=activity&site=stackoverflow')

print(response.json())