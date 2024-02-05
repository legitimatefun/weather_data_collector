# Weather Data Collector

Simple script + systemd service file to collect weather data for selected cities 

## Steps to Use

1. Create mongodb instance with your favourite provider. 
2. Get an API key from https://www.weatherapi.com/
3. Make directory: 'mkdir ~/collect_weather' and cd to directoru
4. Clone files to ~/collect_weather
5. Build virtual environment with pipenv: pipenv install --python 3.9 Pip file lists dependencies
7. Copy collect_weather_data.service service file to your favourite systemd system folder:
    - /etc/systemd/system
    - /usr/lib/systemd/system
    - /lib/systemd/system 
8. Run 'sudo systemctl daemon-reload'
9. Run 'sudo systemctl enable weather-data-collector.service --now
10. You can check if it started correctly by running 'systemctl status weather-data-collector.service

*Secrets file will ask for you to input your mongo db uri and weather API key. No secrets are stored.
