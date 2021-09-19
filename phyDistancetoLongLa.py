import geocoder
address = input("Please enter your address")
g = geocoder.google(address)
print(g.latlng)

