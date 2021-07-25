from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api
import requests
from config import Config

app = Flask(__name__)

HEADERS = {
    'x-rapidapi-key': Config.WEATHER_API_KEY,
    'x-rapidapi-host': Config.WEATHER_API_HOST
}


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    weather = []
    cities = request.form.get("cities")
    cities = cities.replace(" ", " ")
    cities_req = cities.split(",")
    for city in cities_req:
        querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "", "type": "link, accurate", "lat": "",
                       "units": "metric"}

    response = requests.request("GET", Config.WEATHER_API_URL, headers=HEADERS, params=querystring)
    if response.status_code == 200:
        data = response.json()
        try:
            weather.append(data['list'][0])
        except(IndexError,):
            return Response(status=404)
    else:
        return Response(status=404)
    return render_template("weather.html", weather=weather)


@app.route('/search_l_l', methods=['POST'])
def search_weather_l_l():
    weather = []
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    querystring = {"q": "", "cnt": "1", "mode": "null", "lon": lon, "type": "link, accurate", "lat": lat,
                   "units": "metric"}

    response = requests.request("GET", Config.WEATHER_API_URL, headers=HEADERS, params=querystring)
    data = response.json()

    if response.status_code == 200:
        weather.append(data['list'][0])
        return render_template("weather.html", weather=weather)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

