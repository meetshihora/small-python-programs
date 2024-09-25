from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

a = input("Enter the zipcode: ")
zipcode = a

location = geolocator.geocode(zipcode)

print("zipcode: ", zipcode)
print("Ditail of the zipcode: ", location)