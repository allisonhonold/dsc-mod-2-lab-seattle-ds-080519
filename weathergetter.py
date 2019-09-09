import requests

# Powered by Dark Sky <https://darksky.net/poweredby/>
class WeatherGetter():
    """This class gets the weather for Berlin. Using Dark Sky's API"""
    def __init__(self):
        self.lat = '52.520008'
        self.long = '13.404954'
        self.base_url = 'https://api.darksky.net/forecast/45cb5fc5fb6ea6a640aec35533e5f921/'
        self.precip_dict = {}
    
    def get_weather(self, date):
        "Gets the weather for Berlin. Takes date as a string in yyyy-mm-dd"
        if date not in self.precip_dict:
            time = date + "T12:00:00"
            response = requests.get(self.base_url + self.lat + ',' + self.long + ',' + time 
                                    + '?exclude=currently,minutely,hourly,alerts,flags')
            dictionary = response.json()
            weather = dictionary['daily']['data'][0]
            self.precip_dict[date] = weather['precipIntensityMax']>0
        return self.precip_dict[date]

def main():
    pass

if __name__== "__main__":
    main()