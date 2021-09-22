import datetime
import numpy
import requests

from flask import Flask, jsonify, request
from geopy.geocoders import Nominatim

app = Flask(__name__)


@app.route("/weather", methods=['GET'])
def get_weather():
    app.config['JSON_SORT_KEYS'] = False
    city = request.args.get('city')
    days = int(request.args.get('days'))

    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=days)

    locator = Nominatim(user_agent="my_request")
    location = locator.geocode(city)
    longitude = location.longitude
    latitude = location.latitude

    temperature = []
    humidity = []
    pressure = []

    for i in range(days):
        date = end_date - datetime.timedelta(days=i)
        url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'
        api_key = open("api_key.txt", "r").read()
        params = {'lat': latitude, 'lon': longitude, 'dt': int(date.timestamp()),
                  'appid': api_key, 'units': 'metric'}
        response = requests.get(url=url, params=params)
        result = response.json()
        temperature.append(result['current']['temp'])
        humidity.append(result['current']['humidity'])
        pressure.append(result['current']['pressure'])

    temp = {'average': numpy.mean(temperature), 'median': numpy.median(temperature), 'min': numpy.min(temperature),
            'max': numpy.max(temperature)}
    hum = {'average': numpy.mean(humidity), 'median': numpy.median(humidity), 'min': numpy.min(humidity),
           'max': numpy.max(humidity)}
    pres = {'average': numpy.mean(pressure), 'median': numpy.median(pressure), 'min': numpy.min(pressure),
            'max': numpy.max(pressure)}

    answer = {"city": city,
              "from": start_date.strftime("%Y-%m-%d"),
              "to": end_date.strftime("%Y-%m-%d"),
              "temperature_c": {
                  "average": temp['average'],
                  "median": temp['median'],
                  "min": float(temp['min']),
                  "max": float(temp['max']),
              },
              "humidity": {
                  "average": hum['average'],
                  "median": hum['median'],
                  "min": float(hum['min']),
                  "max": float(hum['max']),
              },
              "pressure_mb": {
                  "average": pres['average'],
                  "median": pres['median'],
                  "min": float(pres['min']),
                  "max": float(pres['max'])
              }
              }

    return jsonify(answer)


if __name__ == "__main__":
    app.run(debug=True)
