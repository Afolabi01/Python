#This is a simple illustration of using the request module to interact with an API(last fm)
#First import the module
import requests

ask = input("what artist are you looking for today: ")

#create a request and save it in the response variable or any name you want to call it
response = requests.get("http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist="+ask+"&api_key=&format=json")

#Then derive your results in json form
results = response.json()
name = results['artist']['name']
listeners = results['artist']['stats']['listeners']
plays = results['artist']['stats']['playcount']

#Print out your results using the print function
print('This is ' + name)
print('He has ' + listeners + ' listeners and his music has been played ' + plays + ' times')
