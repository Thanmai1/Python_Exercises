'''Re-write the earlier question of S02Q02 using functions :

     - Using the starting and ending values of your car’s odometer, 
            calculate its mileage'''

def mileage():
    strv = input("Enter the starting value of odometer:")
    endv = input("Enter the ending value of odometer:")
    fuel = input("Enter the amount of fuel:")
    if (strv>endv):
        print("Starting value should be less than ending value")
    else:
        mileage = (int(endv) - int(strv))/int(fuel)
        print("The mileage is", mileage, "km per liter")

#Main starts here

mileage()
