# request_module_for_https
import requests
r = requests.get('file:///C:/Users/Dnyane/Downloads/websites/100%20books/100%20Books%20to%20Read%20Before%20You%20Die%20_%20Reedsy%20Discovery.html')
print(r)
print(r.status_code)

url = 'https://m.youtube.com
data = { 'p1': 1,'p2':2}
r2 = requests.post(url = url, data = data)