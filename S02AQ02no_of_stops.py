'''Re-write the earlier question of S02Q02 using functions :

     - Using the starting and ending values of your car’s odometer, 
            and the measure of fuel consumed, 
            calculate the number of stops one should make for refuelling 
            while travelling from Bangalore to Goa, 
            a distance of 560 kms.'''

def mileage():
    strv = input("Enter the starting value of odometer:")
    endv = input("Enter the ending value of odometer:")
    fuel = input("Enter the amount of fuel:")
    
    if (strv>endv):
        print("Starting value should be less than ending value")
    else:
        mileage = (int(endv) - int(strv))/int(fuel)
        print("The mileage is", mileage, "km per liter")

    return(mileage, strv)

#main starts here

mil, strv1 = mileage()

stopsendv = int(strv1)+560
stops = stopsendv / mil
print("The number of stops required is:", round(stops))
