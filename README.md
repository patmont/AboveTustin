# FlightAnnouncement
[FlightAnnouncement] uses text-to-speech to announce flight and route information of overhead aircraft. Aircraft data is recieved using ATS-B data recieved using a local radio reciever (SDR), flight information is looked up against a csv file.

* Uses [dump1090-mutability](https://github.com/mutability/dump1090) for ADSB message decoding, airplane tracking, and webserving.
* Uses [flightdata] to receive flight data over http
* Uses [

## Example
http://patmont.net/blog/index.php/2016/11/21/overhead-flight-announcement-project/

![Raspberry Pi3 ADSB Receiver] http://patmont.net/blog/wp-content/uploads/2016/11/IMG_2418-768x576.jpg

## Dependencies
* Uses [dump1090-mutability](https://github.com/mutability/dump1090) for ADSB message decoding, airplane tracking, and webserving.
* Uses Google Text To Speech [gTTS](https://github.com/pndurette/gTTS)
* Uses [Pandas]
