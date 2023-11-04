import requests
'''
create a portion of code that will gather the api calls and 
'''

# Define the API endpoint
api_url = "https://api.example.com/user/1"  # Replace with the actual API URL

try:
    # Make a GET request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Access the "name" field from the JSON data
        duration = data["duration"]
        status = data["status"]
        base = data["base"]

        print("Hours:", duration)
        print("Pilot Status:", status)
        print("Home Base:", base)


    else:
        print(f"API request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"API request failed with an exception: {e}")
    
'''
if the cards parameters matches the user parameters such as the type of aircraft, the hours of time as
long as its within the duration of the hours the pilot has left, 
'''