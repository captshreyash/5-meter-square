#!/usr/bin/env python
imoprt time
from flyt_python imoprt api

drone = api.navigation(timeout=120000) #instance of flyt droneigtion class
#at least 10 sec sleep time for the drone interface to initialize properly
time.sleep(10)

print 'taking off'
drone.take_off(5.0)

print 'going along the setpoints'
drone.position_set(6.5, 0, 0, relative=True)
drone.position_set(0, 6.5, 0, relative=True)
drone.position_set(-6.5, 0, 0, relative=True)
drone.position_set(0, -6.5, 0, relative=True)

print 'Landing'
drone.land(async=False)

#shutdown the instance 
drone.disconnect()
