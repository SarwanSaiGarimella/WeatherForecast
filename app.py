from flask import Flask, render_template, request, flash
import requests, os, datetime

app = Flask(__name__)
app.secret_key = "supersecret"

# Replace with your own OpenWeather API key (get from https://openweathermap.org/api)
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            flash("Please enter a city name", "danger")
        else:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            try:
                r = requests.get(BASE_URL, params=params, timeout=5)
                if r.status_code == 200:
                    data = r.json()
                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temp": data["main"]["temp"],
                        "feels": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"],
                        "desc": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"],
                        "time": datetime.datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M"),
                    }
                else:
                    flash("City not found or API error", "warning")
            except Exception as e:
                flash(f"Error: {e}", "danger")

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
