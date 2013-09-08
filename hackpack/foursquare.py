import json
import urllib2
import urllib

def CompressURL(url):
	apiurl = "http://to.ly/api.php?longurl="
	quoted = urllib.quote_plus(url)
	shorturl = urllib.urlopen(apiurl + quoted).read()
	return shorturl

def parseBody(string):
	splitted = string.split(" ")
	location = splitted[0] + " " + splitted[1]
	category = splitted[2]
	data = [location, category]
	return data


def search(location, category):
	location = urllib.quote(location)
	category = urllib.quote(category)
	url = "https://api.foursquare.com/v2/venues/explore?mode=url&near=" + location + "&query=" + category + "&client_id=QD350G42SFQ2PZUP3JLWAF5U453UEKX3RFDJOFKUIRUESXDU&limit=10&client_secret=4BFGFNV4M0IP0J1GIMUKKIFTZ5VDJTYCCGXECRCWAND3TZSP&v=20130907"
	# print url
	data = json.load(urllib2.urlopen(url))
	compressedURL = CompressURL(data["response"]["groups"][0]["items"][0]["venue"]["canonicalUrl"])

	reply= [data["response"]["groups"][0]["items"][0]["venue"]["name"], data["response"]["groups"][0]["items"][0]["location"][0]["address"], compressedURL]
	return reply


def main():
	# data = search("New Brunswick, NJ", "coffee")
	print data[0]
	print data[1]
	
if __name__ == "__main__":
	main()
