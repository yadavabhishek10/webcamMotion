import requests

# Scrap response from below url using IP address of the system
response = requests.get('https://ipinfo.io/')
loc_tracker = response.json()

# Country from the response
country = loc_tracker['country']
if country == "IN":
    country = "India"

# State from the response
state = loc_tracker['region']

# City from the response
city = loc_tracker['city']

# Latitude and Longitude from the response
location = loc_tracker['loc'].split(',')
latitude = location[0]
longitude = location[1]

# Print all the above location parameters
print("Country: {0}".format(country))
print("State: {0}".format(state))
print("City: {0}".format(city))
print("Latitude: {0}".format(latitude))
print("Longitude: {0}".format(longitude))
