"""
Project 2 - Moonlander

Name: Derek Sit
Instructor: Mike Ryu
Section: 13

"""

from landerFuncs import *

showWelcome()
alt = getAltitude()
fuel = getFuel()
print("\nLM state at retrorocket cutoff")
displayLMState(0, alt, 0.00, fuel, 0)
print("")
fuelRate = getFuelRate(fuel)
vel = 0.00
accel = 0.0
time = 0

while alt > 0:
	accel = updateAcceleration(1.62, fuelRate)
	fuel = updateFuel(fuel, fuelRate)
	alt = updateAltitude(alt, vel, accel)
	vel = updateVelocity(vel, accel)
	time = time + 1
	if fuel > 0 and alt != 0:
		displayLMState(time, alt, vel, fuel, fuelRate)
		print("")
	elif alt > 0:
		print("OUT OF FUEL - Elapsed Time: {:>3}".format(time), "Altitude: {:>7.2f}".format(round(alt, 2)), "Velocity: {:>7.2f}".format(round(vel, 2)))
	fuelRate = getFuelRate(fuel)

if alt < 0:
    print("\nLM state at landing/impact")
    alt = 0
    displayLMState(time, 0, vel, 0, 0)

print("")
displayLMLandingStatus(vel)
