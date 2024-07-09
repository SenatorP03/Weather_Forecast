# Import the required libraries
import requests
API_KEY = "914c2a68d0fa3524221f89a610e30d84"

# define a function to get data and get require response
def get_data(place = None, forecast = None, kind = None):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q="
           f"{place}&appid={API_KEY}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast
    filtered_data = filtered_data[:nr_values]
    return filtered_data

# conditionally statement to checks
if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast=3,kind="Temperature"))