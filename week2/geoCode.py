import httplib2
import json


google_geocode_id = ""

fsid = ""
fsSecret = ""

def getGeocodeLocation(inputString):
	locationString = inputString.replace(" ","+")
	url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s"%(
		locationString, google_geocode_id))
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	return result


def findAResturant(mealType, location):

	pass todo
