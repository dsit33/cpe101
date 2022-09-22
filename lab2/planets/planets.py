def weight_on_planets():
   # write your code here
   userWeight = input("What do you weigh on earth?")
   userWeight = float(userWeight)
   print("\nOn Mars you would weigh " + "{:.2f}".format(userWeight * .38) + " pounds.")
   print("On Jupiter you would weigh " + "{:.2f}".format(userWeight * 2.34)  + " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()