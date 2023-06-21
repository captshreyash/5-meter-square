#!/usr/bin/env python
import time
from flyt_python imoprt api

drone = api.navigation(timeout=120000)

#at least 10sec sleep time for the drone interface to initiaize properly
time.sleep(10)

print 'taking off'
drone.take_off(10.0)

print 'going along the setpoints'
drone.position_set(10, 0, 0, relative=True)
drone.position_set(0, 10, 0, relative=True)
drone.position_set(-10, 0, 0, relative=True)
drone.position_set(0, -10, 0, relative=True)

print 'Landing'
drone.land(async=False)

#shutdown the instance
drone.disconnect()
