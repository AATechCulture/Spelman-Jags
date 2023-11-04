import requests
'''
create a portion of code that will gather the api calls and 
'''

# Define the API endpoint
user_api = "https://api.example.com/user/1"  # Replace with the actual API URL
flight_api = "https://api.example.com/user/1" 

try:
    # Make a GET request to the API
    response = requests.get(user_api)

    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Access the "name" field from the JSON data
        user_duration = data["duration"]
        user_status = data["status"]
        user_base = data["base"]

        flight_duration = data["duration"]
        flight_status = data["status"]
        flight_base = data["base"]

        if (user_duration == flight_duration):
            print("Hours", flight_duration)
            print("Pilot Status:", flight_status)
            print("Home Base:", flight_base)

    else:
        print(f"API request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"API request failed with an exception: {e}")

'''
This is a new feature that is going to be added to the pbs they already have

if the cards parameters matches the user parameters such as the type of aircraft, the hours of time as
long as its within the duration of the hours the pilot has left, 
'''