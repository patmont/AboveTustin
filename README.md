# FlightAnnouncement
[FlightAnnouncement] uses text-to-speech to announce flight and route information of overhead aircraft. The motivation for this project is hobby airplane traffic monitoring while living nearby heavily traveled flight paths. Project is tested on stand-alone/headless Raspberry Pi 3 running Rasbian Jesse with RTL-SDR "Gen 1" receiver.

## Function
* Flight Number, Distance, and Altitude received by SDR and demodulated by Dump1090-mutability
* Flight Data returned over http in JSON
* Flights are indexed by hex ID until alarm status is met
* Since ADS-B messages do not contain origin/destination data, the flight number is searched in a dataframe lookup. This data (included in csv) is the result of merging [virtualradarserver.co.uk](http://www.virtualradarserver.co.uk/FlightRoutes.aspx) and [openflights.org](http://openflights.org/data.html).
* Announcement string is formed, intended to be concise and conversational
* Announcement string is converted to mp3 format using google translate API and played back

## Example
http://patmont.net/ads-b-flight-path-visualization/

![Raspberry Pi3 ADSB Receiver](http://patmont.net/blog/wp-content/uploads/2016/11/IMG_2418-768x576.jpg)

## Dependencies

* Uses [gr-osmosdr](https://github.com/osmocom/gr-osmosdr) for radio driver
* Uses [dump1090-mutability](https://github.com/mutability/dump1090) for ADSB message decoding, airplane tracking, and webserving.
* Uses Google Text-To-Speech [gTTS](https://github.com/pndurette/gTTS). Requires internet connection
* Uses [Pandas]

## Improvements
* Flight Route csv is not completly reliable. Prefer flight route data is pulled from web, many popular sites are pay-per-query API.
* The csv file could be supplemented by ACARS data; this would require a 2nd data source and handling.
* Offline mode to replace gTTS. I could not find a working repo for Python 3.
