''' A Chemical plant has a tank for storing ethanol.
            - When the tank is more than 80% full, it
                 should raise an alarm to close the valve.
            - When the tank is less than 20% full, it
                 should send an SMS to buy more liquid.
            - The total tank capacity is 900 litres.
            - Write a program to simulate this.
            - Ask user to enter current level of ethanol in the tank.
            - Print the appropriate action based on value entered
            - Make sure that your program needs minimum changes
                 for a tank of different capacity.'''

def do_action(present, redmark, bluemark):
    if present > redmark:
        print("Please close the value, tank is more than 80% full")
    if present < bluemark:
        print("Please buy more liquid, tank is less that 20% full")
    if present > bluemark and present < redmark:
        print("The current level of the tank is", present)

def get_current_level():
    value = input("Enter the current level:")
    return int(value)

# Main starts from here
capacity = 900
high = int(capacity)*0.8
low = int(capacity)*0.2
level = get_current_level()
do_action(level, high, low)
