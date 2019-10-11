import requests
import json

# Powered by Dark Sky <https://darksky.net/poweredby/>

# load secret key
with open("~/.secrets/dark_sky_api.json", "r") as f:
    key = json.load(f)['key']

class WeatherGetter():
    """This class gets the weather for Berlin. Using Dark Sky's API"""


    def __init__(self):
        self.lat = '52.520008'
        self.long = '13.404954'
        self.base_url = f"https://api.darksky.net/forecast/'
        self.precip_dict = {}
    
    def get_weather(self, date):
        "Gets the weather for Berlin. Takes date as a string in yyyy-mm-dd"
        if date not in self.precip_dict:
            time = date + "T12:00:00"
            response = requests.get(self.base_url + key + '/' + self.lat + ',' + self.long + ',' + time 
                                    + '?exclude=currently,minutely,hourly,alerts,flags')
            dictionary = response.json()
            weather = dictionary['daily']['data'][0]
            self.precip_dict[date] = weather['precipIntensityMax']>0
        return self.precip_dict[date]

def main():
    pass

if __name__== "__main__":
    main()