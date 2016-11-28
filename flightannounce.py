
# coding: utf-8

# In[ ]:

#
# "Overhead Flight Announce" by pat@patmont.net 11/27/2016
#
# forked from kevinabrandon@gmail.com
#
# Dependecies: python 3 dump1090-mutability flightdata.py gTTS pygame fnaccounce.py pandas
# Update lines 28-32 in flightdata.py for your location

import sys
from time import sleep
from datetime import *
import flightdata
from gtts import gTTS
from pygame import mixer
from fnannounce import fnannounce

# variables for below
distanceAlarm = 5 	# the alarm distance in miles.
elevationAlarm = 50 # the angle in degrees that indicates if the airplane is overhead or not.
nCoast = 1			# number of updates to wait after the airplane has left the alarm zone before tweeting.
sleepTime = 0.5 	# time between each loop.

# variables for fnannounce.py
myCtry = 'United States'
myICAO = ['KSFO', 'KSJC', 'KOAK']


# In[ ]:

fd = flightdata.FlightData()
lastTime = fd.time

alarms = dict() # dictonary of all aircraft that have triggered the alarm
                # Indexed by it's hex code, each entry contains a tuple of
                # the aircraft data at the closest position so far, and a 
                # counter.  Once the airplane is out of the alarm zone,
                # the counter is incremented until we hit [nCoast] (defined
                # above), at which point we then Tweet
finishedalarms = []
    
while True:
    try:
        sleep(sleepTime) #set pause duration
        fd.refresh()
        if fd.time == lastTime:
            continue
        lastTime = fd.time

        current = dict() # current aircraft inside alarm zone

        # loop on all the aircarft in the receiver
        for a in fd.aircraft:
            # if they don't have flight or lat or lon, skip them
            if a.flight == "N/A" or a.lat == None or a.lon == None: 
                continue

            # check to see if it's in the alarm zone:
            if a.distance < distanceAlarm:
                # add it to the current dictionary
                current[a.hex] = a 

                if a.hex in alarms:
                    #if it's already in the alarms dict, check to see if we're closer
                    if a.distance < alarms[a.hex][0].distance:
                        #if we're closer than the one already there, then overwrite it
                        alarms[a.hex] = (a, 0)
                else:
                    #add it to the alarms
                    alarms[a.hex] = (a, 0)

            if a.hex in alarms:
                #if it's already in the alarms dict, check to see if it is getting farther
                if a.distance > alarms[a.hex][0].distance:
                    #if the flight has already been announced, then skip
                    if a.hex in finishedalarms:
                        pass
                    #if the flight has not been anounced
                    else:
                        try:
                            fnannounce(a.flight, a.altitude, myCtry, myICAO)
                            
                            # Now add it to the finished alarms index
                            finishedalarms.append(a.hex)
                        except:
                            # Add it to the finished alarms index
                            finishedalarms.append(a.hex)

    except:
        print('No flights in range. Trying again.')

