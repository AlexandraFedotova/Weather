import datetime
import numpy
import requests
import os

from flask import Flask, jsonify, request

app = Flask(__name__)
api_key = os.environ.get('API_KEY')


@app.route("/")
def welcome():
    welcome_page = "<p> The right form of request to the weather-service: /weather?city=&ltcity>&days=&ltn>. </p>"
    return welcome_page


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

    url = 'http://api.weatherapi.com/v1/history.json'
    params = {'key': api_key, 'q': city, 'dt': 0}

    for i in range(n):
        params['dt'] = (end_date - datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        response = requests.get(url=url, params=params)

        if response.status_code == 200:
            result = response.json()
        else:
            return {'status_code': response.status_code, 'message': 'Problem getting Json data from response. '}

        data = result['forecast']['forecastday'][0]

        temperature.append(data['day']['avgtemp_c'])
        humidity.append(data['day']['avghumidity'])
        pressure.append(data['hour'][11]['pressure_mb'])

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
