# Weather Forecast Web App (Flask + OpenWeather API)

## Features
- Search any city for live weather (temp, feels like, humidity, description)
- Data from **OpenWeather API**
- Attractive Bootstrap UI
- Ready for Cloud Deployment (Heroku/AWS)

## Run Locally
1. Get an API key from https://openweathermap.org/api
2. Set it in environment variable:  
   Windows: `set OPENWEATHER_API_KEY=yourkey`  
   macOS/Linux: `export OPENWEATHER_API_KEY=yourkey`
3. Install requirements:  
   `pip install -r requirements.txt`
4. Run app:  
   `python app.py`
5. Open: http://localhost:5000

## Deploy to Cloud
- Use `gunicorn` for production: `gunicorn app:app`
- On Heroku: set `OPENWEATHER_API_KEY` as Config Var.
- On AWS: run inside EC2 or Elastic Beanstalk, same config.
