"""
Name: Derek Sit
Instructor: Mike Ryu
Section: 13

"""
from funcs import *

def main():
   userWeight = float(input("How much do you weigh (pounds)?"))
   distance = float(input(" How far away is your professor (meters)?"))
   thrownObject = input(" Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")

   objMass = getMassObject(thrownObject)
   objVel = getVelocityObject(distance)
   userKG = poundsToKG(userWeight)

   skaterVel = getVelocitySkater(userKG, objMass, objVel)

   if objMass <= 0.1:
   		comment = "You're going to get an F!"
   if objMass > 0.1 and objMass <= 1.0:
   		comment = "Make sure your professor is OK."
   if objMass > 1.0:
   		if distance < 20:
   			comment = "How far away is the hospital?"
   		else:
   			comment = "RIP professor."

   print("\nNice throw! " + comment)
   print("Velocity of skater: " + '{:.3f}'.format(skaterVel) + " m/s")
   if skaterVel < 0.2:
         print("My grandmother skates faster than you!")
   if skaterVel >= 1.0:
         print("Look out for that railing!!!")

if __name__ == '__main__':
   main()