# PROG 1: City Latitude and Longitude Lookup

# Write The Code Here
cities = {
    'mumbai': (19.076, 72.8777),
    'bangalore': (12.9716, 77.5946),
    'chennai': (13.0827, 80.2707),
    'pune': (18.5204, 73.8567),
    'hyderabad': (17.385, 78.4867)
}


def check_city(city):
    city = city.lower()

    if city in cities:
        latitude, longitude = cities[city]
        return f"{city.title()}: Latitude = {latitude}, Longitude = {longitude}"
    else:
        return "City not found in the dictionary."


print("Cities Dictionary:")
print(cities)

while True:
    city = input("Enter a city name (or type 'exit' to quit): ")

    if city.lower() == "exit":
        print("Exiting the program.")
        break

    result = check_city(city)
    print(result)