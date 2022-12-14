import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "org": response.get("org"),
        "asn": response.get("asn"),
        "country_code": response.get("country_code")
    }


    return location_data
    
out = get_location()


data = "IP: " + out.get('ip') + "\nCity: " + out.get('city') + "\nRegion: " + out.get('region') + "\nCountry: " + out.get('country') + "\nISP: " + out.get('org') + "\nASN: " + out.get('asn') + "\nCountry code: "+ out.get('country_code')



import pyautogui


displayText = 'Send request to IP-API to display IP, Geolocation, Internet Provider, ASN, and Country Code?'

a = pyautogui.confirm(text=displayText, title='Social Coding Application', buttons=['Send', 'Cancel'])

if a=="Send":
    pyautogui.alert(text=data, title='Social Coding Application', button='OK')
