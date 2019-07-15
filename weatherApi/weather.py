import pyowm
apiKey = '2cac2a2f1a4907ada47ba637b9c3686f'
#apiKey = 'bf45390a352169d3a24e4ea5363c3c49'
owm = pyowm.OWM(apiKey)
#observation = owm.weather_at_place('London,uk')



 
#w.get_wind()
#w.get_humidity()

li = []

countries = {
    'gh':'Ho',
    'uk':'London',
    'ng':'Lagos'
    }


for keys,values in countries.items():
     print(keys+ ' '+ values)
     k = values+','+keys
     observation = owm.weather_at_place(str(k))
     w = observation.get_weather()
     
     print('wind: ',w.get_wind())
     print('humidity: ',w.get_humidity())
     print('\n')

