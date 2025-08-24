import requests
api_key="267bb767f5d622261e31e108da9e888d"
lat= 1.29
lon= 36.82
url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
response=requests.get(url)
# print(response.status_code)
# print(response.json())
data=response.json()
# coordinates= data['coord']
# print(coordinates)
# print("longitude:", coordinates['lon'])
# print("latitude:", coordinates['lat'])
# print("Name:", data['name'])
print(data['main']['temp'])