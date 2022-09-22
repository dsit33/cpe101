"""
Project 5 - Earthquakes

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

from quakeFuncs import *

quakes = read_quakes_from_file("quakes.txt")
print("")
print("Earthquakes:")
print("------------")
for quake in quakes:
	print(quake)
user = ''
while user != 'q':
	newList = []
	print("")
	print("Options:")
	print("  (s)ort")
	print("  (f)ilter")
	print("  (n)ew quakes")
	print("  (q)uit")
	print("")
	user = input("Choice: ").lower()

	if user == 's':
		sort = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or (l)atitude? ").lower()
		print("")
		print("Earthquakes:")
		print("------------")
		if sort == 'm':
			for quake in sorted(quakes, key = attrgetter('mag'), reverse = True):
				print(quake)
			quakes = sorted(quakes, key = attrgetter('mag'), reverse = True)
		if sort == 't':
			for quake in sorted(quakes, key = attrgetter('time'), reverse = True):
				print(quake)
			quakes = sorted(quakes, key = attrgetter('time'), reverse = True)
		if sort == 'l':
			for quake in sorted(quakes, key = attrgetter('longitude'), reverse = False):
				print(quake)
			quakes = sorted(quakes, key = attrgetter('longitude'), reverse = False)
		if sort == 'a':
			for quake in sorted(quakes, key = attrgetter('latitude'), reverse = False):
				print(quake)
			quakes = sorted(quakes, key = attgetter('latitude'), reverse = False)
	if user == 'f':
		filtBy = input("Filter by (m)agnitude or (p)lace? ").lower()
		if filtBy == 'm':
			low = input("Lower bound: ")
			high = input("Upper bound: ")
			print("")
			print("Earthquakes:")
			print("------------")
			newList = filter_by_mag(quakes, low, high)
			for quake in newList:
				print(quake)
			newList = []
		if filtBy == 'p':
			string = input("Search for what string? ").lower()
			print("")
			print("Earthquakes:")
			print("------------")
			newList = filter_by_place(quakes, string)
			for quake in newList:
				print(quake)
			newList = []
	if user == 'n':
		seen = False
		print("")
		print("New quakes found!!!")
		print("")
		print("Earthquakes")
		print("------------")
		url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"
		jsonList = get_json(url)
		features = jsonList["features"]
		for feature in features:
			newQuake = quake_from_feature(feature)
			newList.append(newQuake)
			for new in newList:
				for quake in quakes:
					if new == quake:
						seen = True
				if seen == False:
					quakes.append(new)
				seen = False
		for quake in quakes:
			print(quake)
	if user == 'q':
		file = open("quakes.txt", "w")
		for quake in quakes:
			file.write("{}".format(quake.mag) + " {}".format(quake.longitude) + " {}".format(quake.latitude) + " {}".format(quake.time) + " {}".format(quake.place)+"\n")
		file.close()
		exit()




