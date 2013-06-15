from xml.etree import ElementTree
from math import sqrt
import urllib2
import StringIO


#Compute distance from every other station and cache the ordered nearest station list for each station. Run once per (x period) to keep it up to date with new stations.

#Computer ratio of bikes to empties.  Go from highest percentage to nearest lowest percentage. But give score by mulitplying by full size? Need to think more.

#Then show which bikes need to be ridden (or driven) to which nearby stations.


p = urllib2.urlopen('http://www.capitalbikeshare.com/data/stations/bikeStations.xml')
c = p.read()
tree = ElementTree.parse(StringIO.StringIO(c))

def slicedict(d, s):
	return {k:v for k,v in d.iteritems() if k.startswith(s)}




def bikeshare_samaratin(station_number):

	location_dict = {}
	station_info_dict = {}
	station_pairs_list = []
	id_num_list = []
	for station in tree.findall('station'):
		id_num = int(station.find('id').text)
		name = station.find('name').text
		lat = float(station.find('lat').text)
		lon = float(station.find('long').text)
		location_dict[id_num] = { "name":name, "location":(lat,lon)}
		station_size = float(station.find('nbBikes').text) + float(station.find('nbEmptyDocks').text)
		pct_full = round(float(station.find('nbBikes').text)/(station_size + .0000000001)*100,0)
		pct_weighted = pct_full * station_size
		id_num_list += [id_num]
		station_info_dict[id_num] = {"name":name,"station_size":station_size, "pct_full":pct_full}

	for id,num in enumerate(id_num_list):
		for item in id_num_list[:id]:
			station_pairs_list += [(num, item, sqrt(((location_dict[num]['location'][0]-location_dict[item]['location'][0])**2)+(location_dict[num]['location'][1]-location_dict[item]['location'][1])**2))]


	station_pairs_list.sort(key=lambda tup: tup[2])

	station_pairs = [list(elem) for elem in station_pairs_list]

	#print list_final

	focus_station_pairs = [item for item in station_pairs if station_number in item]

	#print focus_station_pairs


	for i in focus_station_pairs:
		if station_info_dict[i[0]]['pct_full'] > station_info_dict[i[1]]['pct_full']:
			print station_info_dict[i[0]]['name'] + " <- " + station_info_dict[i[1]]['name']
		elif station_info_dict[i[0]]['pct_full'] < station_info_dict[i[1]]['pct_full']:
			print station_info_dict[i[0]]['name'] + " -> " + station_info_dict[i[1]]['name']
		elif  station_info_dict[i[0]]['pct_full'] == station_info_dict[i[1]]['pct_full']:
			print station_info_dict[i[0]]['name'] + " == " + station_info_dict[i[1]]['name']


bikeshare_samaratin(52)





