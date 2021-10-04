import datetime
import numpy
import requests
import os

from flask import Flask, jsonify, request

app = Flask(__name__)
api_key = os.environ.get('API_KEY')


@app.route("/weather", methods=['GET'])
def get_weather():
    app.config['JSON_SORT_KEYS'] = False
    city = request.args.get('city')
    n = int(request.args.get('days'))

    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=n)

    temperature = []
    humidity = []
    pressure = []

    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
    url += city + '/' + start_date.strftime('%Y-%m-%d') + '/' + end_date.strftime('%Y-%m-%d')
    params = {'key': api_key, 'unitGroup': 'metric', 'elements': 'temp,humidity,pressure', 'include': 'days'}
    response = requests.get(url=url, params=params)
    try:
        result = response.json()
    except ValueError:
        return {'staus_code': response.status_code, 'url': url, 'params': params}

    days = result['days']
    for day in days:
        temperature.append(day['temp'])
        humidity.append(day['humidity'])
        pressure.append(day['pressure'])

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
    app.run(debug=True, host='0.0.0.0')
