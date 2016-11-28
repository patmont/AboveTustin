
# fnannounce.py
#
# pat@patmont.net 11/27/2016

from pandas import read_csv
import re
from gtts import gTTS
from pygame import mixer

df = read_csv('FlightRouteLocationNames_UTF.csv')

def fnannounce(fn, altitude, home_ctry, home_ICAO):
    
    # takes flight number in format 'SAS935' format and returns a brief announcement
    # see CSV file for naming format

    # split flight number string
    fn = re.split('(\d+)',fn)

    #return flight info from "df"
    info = df[(df['ICAO']== fn[0]) & (df['FlightNumber']== fn[1])]

    ####### if a is not blank 

    # define local variables
    carrier = info.iloc[0][0]
    flightno = fn[1]
    origin_ICAO = info.iloc[0][4]
    origin_city = info.iloc[0][6]
    origin_ctry = info.iloc[0][7]
    dest_ICAO = info.iloc[0][5]
    dest_city = info.iloc[0][8]
    dest_ctry = info.iloc[0][9]

    ## determine inbound/outbound/other
    if origin_ICAO in home_ICAO:
        bound = 'out'
    elif dest_ICAO in home_ICAO:
        bound = 'in'
    else:
        bound = 'other'

    ## determine flight nationality
    if origin_ctry == home_ctry and dest_ctry == home_ctry:
        nationality = 'dom'
    else:
        nationality = 'intl'

    ## create announcement string
    if bound == 'in' and nationality == 'intl':
        # International Arrival
        announcement = "{} flight {} from {}, {}, is arriving at {}.".format(
        carrier, flightno, origin_city, origin_ctry, dest_city)

    elif bound == 'in' and nationality == 'dom':
        # Domestic Arrival
        announcement = "{} flight {} from {}, is arriving at {}.".format(
            carrier, flightno, origin_city, dest_city)

    elif bound == 'out' and nationality == 'dom':
        # Domestic Departure
        announcement = "{} flight {} from {}, is heading to {}.".format(
            carrier, flightno, origin_city, dest_city)

    elif bound == 'out' and nationality == 'intl':
        # International Departure
        announcement = "{} flight {} from {}, is heading to {}, {}.".format(
            carrier, flightno, origin_city, dest_city, dest_ctry)

    elif bound == 'other' and nationality == 'dom':
        # Domestic Other
        announcement = "{} flight {} from {} is crossing through to {}.".format(
            carrier, flightno, origin_city, dest_city)
   
    elif bound == 'other' and nationality == 'intl':
        # International Other
        announcement = "{} flight {} from {}, {} is crossing through to {}, {}.".format(
            carrier, flightno, origin_city, origin_ctry, dest_city, dest_ctry)

    else:
        # Fallback
        announcement = "Flight {}{} is {} feet overhead.".format(fn[0], fn[1], altitude)
        print('Flight is not in the list. Update list and restart.')

    # Google Voice
    tts = gTTS(text=announcement, lang='en-us')
    tts.save("announcement.mp3")
    mixer.init()
    mixer.music.load('announcement.mp3')
    mixer.music.play()
    print(announcement)

