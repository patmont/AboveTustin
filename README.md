# FlightAnnouncement
[FlightAnnouncement] uses text-to-speech to announce flight and route information of overhead aircraft. Aircraft data is recieved using ADS-B data recieved using a local radio reciever (SDR), flight information is looked up against a csv file.

* Flight Number, Distance, and Altitude received by SDR using Dump1090-mutability
* Flight Data returned over http in JSON
* Flights are indexed by hex ID until alarm status is met
* Announcement string is formed, intended to be concise and conversational
* Announcement string is converted to mp3 format using google translate API

## Example
http://patmont.net/blog/index.php/2016/11/21/overhead-flight-announcement-project/

![Raspberry Pi3 ADSB Receiver](http://patmont.net/blog/wp-content/uploads/2016/11/IMG_2418-768x576.jpg)

## Dependencies
* Uses [dump1090-mutability](https://github.com/mutability/dump1090) for ADSB message decoding, airplane tracking, and webserving.
* Uses Google Text To Speech [gTTS](https://github.com/pndurette/gTTS)
* Uses [Pandas]
