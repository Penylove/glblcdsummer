import pyowm
apiKey = '2cac2a2f1a4907ada47ba637b9c3686f'
#apiKey = 'bf45390a352169d3a24e4ea5363c3c49'
owm = pyowm.OWM(apiKey)
#observation = owm.weather_at_place('London,uk')
obs1 = owm.weather_at_place('Hong Kong,china')
obs2 = owm.weather_at_place('Tokyo,japan')
#w = observation.get_weather()
w = obs1.get_weather()
p = obs2.get_weather()

w.get_reference_time()
print(w.get_reference_time())

print(w.get_reference_time(timeformat='date') )

print(w.get_clouds())

print(w.get_rain())
print(w.get_snow())

print(w.get_wind())
print(w.get_humidity())
print(w.get_status())

if w.get_humidity() > p.get_humidity():
    print("Humidity in Hong Kong China high compared to Tokyo Japan ")
elif p.get_humidity() > w.get_humidity():
    print("Humidity in Tokyo Japan is high compared to Hong Kong,China")

