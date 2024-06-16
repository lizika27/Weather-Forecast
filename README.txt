#Weather Forecast

The Weather Forecast Application is a Python-based tool that provides users with real-time weather forecasts for any city they specify. The application leverages the OpenWeatherMap API to retrieve accurate and up-to-date weather information. Users can easily enter the name of a city, and the application will display the current weather conditions along with a forecast for the current moment.

Instruction:

Run "cmd" support python environment variables or other python shell -> type: python main.py

Interaction:
At First, the user will supply the name of the default city to be presented, which will be saved in a JSON file named "defaultCity.json".
Second, the user will be asked to insert the name of the city he wishes to display the weather of.
Finally, each time the program executes, a city name will be asked to be provided, when no city is provided the weather data of the default city will be presented in the console.


## Requirements

python 3.10 and up.

Installing the following packages:

1. datetime - https://pypi.org/project/DateTime/
2. requests - https://pypi.org/project/requests/
3. pytz - https://pypi.org/project/pytz/
4. pycountry_convert - https://pypi.org/project/pycountry/

Imports:

1. datetime  
2. requests 
3. json 
4. pytz 
5. pycountry_convert 
6. os.path 