# DC BikeShare Samaritan

We all love DC BikeShare but it can be frustrating when stations are completely full or empty.  The DC BikeShare van drivers do a great job moving bikes around town, but what if good people like you and me could also move bikes around the city to even up their distribution?

Introducing Bikeshare Samaritan. 

The idea is a simple web app to help you balance the bike load for stations near you.

This `python` code curently works.  It pulls from the live [XML data feed of DC bikeshare](http://www.capitalbikeshare.com/data/stations/bikeStations.xml), then given a station number, it computes the nearest stations and tells you which ones need more bikes or could send bikes to the selected station. 

Output currently looks like this:

    M St & Delaware Ave NE -> 1st & M St NE
    Eckington Pl & Q St NE <- 1st & M St NE
    3rd & H St NE <- 1st & M St NE
    Columbus Circle / Union Station -> 1st & M St NE
    6th & H St NE <- 1st & M St NE
    North Capitol St & F St NW -> 1st & M St NE
    ...
    ...
    ...


Would like to now:
* Create a nice front-end for it.
* Probably migrate it to javascript so it can run client-side.
* Build it so that it is location aware and finds the station nearest to the users current or stated location.

Help welcome!

