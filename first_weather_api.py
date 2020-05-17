import requests
from pprint import pprint


par = {'humidity' : 67}
url = 'http://api.openweathermap.org/data/2.5/weather?q=Nagpur&appid=cb5a9344e2be58d4b34afda137a07217'
r = requests.get(url,params=par)
data = r.json()
print(dir(r))
pprint(data)
#print(r.text)
print(r.url)
pprint(data['main']['humidity'])


