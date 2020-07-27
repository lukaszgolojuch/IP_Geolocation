import requests

print("IP adress or domain name: \n")
query = raw_input()

resp = requests.get("http://ip-api.com/line/"+query+"?fields=status")
status = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=continent")
continent = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=country")
country = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=region")
region = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=city")
city = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=zip")
zip = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=lat")
lattitude = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=lon")
longtitude = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=timezone")
timezone = resp.text
resp = requests.get("http://ip-api.com/line/"+query+"?fields=currency")
currency = resp.text

print("\nStatus: "+ status)
print("Continent: "+ continent)
print("Country: "+ country)
print("Region: "+ region)
print("City: "+ city)
print("Zip: "+ zip)
print("Latitude: "+ lattitude)
print("Longitude: "+ longtitude)
print("Timezone: "+ timezone)
print("Currency: "+ currency)

