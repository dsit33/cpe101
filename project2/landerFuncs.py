"""
Project 2 - Moonlander

Name: Derek Sit
Instructor: Mike Ryu
Section: 13
"""

from math import sqrt

def showWelcome():
    """
    CONTRACT | showWelcome : none -> string
    PURPOSE  | display the welcome message
    EXAMPLES | n/a
    """
    print("\nWelcome aboard the Lunar Module Flight Simulator\n\n   To begin you must specify the LM's initial altitude\n   and fuel level.  To simulate the actual LM use\n   values of 1300 meters and 500 liters, respectively.\n\n   Good luck and may the force be with you!\n")

    # first-outlines


def getFuel():
    """
    CONTRACT | getFuel : none -> int
    PURPOSE  | prompt the user for the amount of fuel
    EXAMPLES | n/a
    """
    fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    while fuel <= 0:
        print("ERROR: Amount of fuel must be positive, please try again")
        fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    return fuel

    # second-outline


def getAltitude():
    """
    CONTRACT | getAltitude : none -> float
    PURPOSE  | prompt user for the altitude of the lander
    EXAMPLES | n/a
    """
    alt = float(input("Enter the initial altitude of the LM (in meters): "))
    while alt < 1 or alt > 9999:
        print("ERROR: altitude must be between 1 and 9999, inclusive, please try again")
        alt = float(input("Enter the initial altitude of the LM (in meters): "))
    return alt

    # third-outline


def getFuelRate(currentFuel):
    """
    CONTRACT | getFuelRate : int -> int
    PURPOSE  | return the user entered value for their fuel rate
    EXAMPLES | n/a
    """
    if currentFuel != 0:
        rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
        if rate < 0 or rate > 9:
            print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
            rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
        if (rate > currentFuel):
            return currentFuel
        else:
            return rate
    else:
        return 0

    # fifth-outline


def displayLMLandingStatus(velocity):
    """
    CONTRACT | displayLMLandingStatus : float -> string
    PURPOSE  | show the status of the LM when it lands
    EXAMPLES | n/a
    """
    if velocity <= 0 and velocity >= -1:
        print("Status at landing - The eagle has landed!")
    elif velocity < -1 and velocity > -10:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    else:
        print("Status at landing - Ouch - that hurt!")

    # sixth-outline


def updateAcceleration(gravity, fuelRate):
    """
    CONTRACT | updateAcceleration : float int -> float
    PURPOSE  | calculate and return the acceleration based on the gravitational constanst and fuel consumption
    EXAMPLES | 1.62 4 -> -.324
             | 1.62 7 -> .648
    """
    return gravity * ((fuelRate/5) - 1)

    # seventh-outline


def updateAltitude(altitude, velocity, acceleration):
    """
    CONTRACT | updateAltitude : float float float -> float
    PURPOSE  | calculate and return the new altitude
    EXAMPLES | 500 3 .6 -> 503.3
    		 | 6032 20 .3 -> 5052.15
    """
    return altitude + velocity + acceleration/2

    # eighth-outline


def updateVelocity(velocity, acceleration):
    """
    CONTRACT | updateVelocity : float float -> float
    PURPOSE  | calculate the new velocity
    EXAMPLES | 20.4 .65 -> 21.05
    		 | 12.46 -.71 -> 11.75
    """
    return velocity + acceleration

    # ninth-outline


def updateFuel(fuel, fuelRate):
    """
    CONTRACT | updateFuel : int int -> int
    PURPOSE  | calculate the existing amount of fuel
    EXAMPLES | 50 7 -> 43
    		 | 33 8 -> 25
    """
    return fuel - fuelRate

    # tenth-outline


def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    """
    CONTRACT | displayLMState : int float float int int -> string
    PURPOSE  | display the state of the lander based on the parameters entered
    EXAMPLES | n/a
    """

    print("Elapsed Time: {:>4}".format(elapsedTime), "s")
    print("        Fuel: {:>4}".format(fuelAmount), "l")
    print("        Rate: {:>4}".format(fuelRate), "l/s")
    print("    Altitude: {:>7.2f}".format(round(altitude, 2)), "m")
    print("    Velocity: {:>7.2f}".format(round(velocity, 2)), "m/s")



    # fourth-outline


