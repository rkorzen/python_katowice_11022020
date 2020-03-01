# pip install requests
import requests

resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/")
print(resp.status_code)
print(resp.content)
for currency in resp.json()[0]['rates']:
    print(currency['currency'], currency['mid'])

https://www.metaweather.com/api/location/search/?query=warsaw
https://www.metaweather.com/api/location/523920/

# python pogoda.py warsaw
# Pogoda w warsaw:
# temperatura: 10 C
# wilgotność:
# ciśnienie