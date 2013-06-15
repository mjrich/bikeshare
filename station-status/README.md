# DC BikeShare Samaratin

We all love DC BikeShare but it can be frustrating with stations are completely full or empty.  The DC BikeShare van drivers do a great job moving bikes around town, but what if good people like you and me could move bikes around the city to even up their distribution?

Introducing Bikeshare Samartin. With a single click, eventually, you'll be able to see the stations nearest to you, and how you could help balance the bike load for it.

This `python` code curently works.  It pulls from the live [XML data feed of DC bikeshare](http://www.capitalbikeshare.com/data/stations/bikeStations.xml), then given a station number, it computes the nearest stations and tells you which ones need more bikes or could send bikes to the selected station.  

Would like to now:
1. Create a nice front-end for it.
2. Migrate it to javascript so it can run client-side.
3. Build it so that it is location aware and finds the station nearest to the users current or stated location.


