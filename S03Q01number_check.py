''' Take 2 numbers from the user. 
            Print which number is a 2 digit number, 
            and which number is a 3 digit number. 
            If it is neither, then print the number as it is'''

def perform_check(number):
    if (number < 9) or (number > 999):
        print(" The number is ",int(number))
    if (number > 9) and (number <= 99):
        print("It is a 2 digit number")
    if (number > 99) and (number <= 999):
        print("It is a 3 digit number")
    
        

def get_number():
    num = input("Enter the number here:")
    return (int(num))

#main starts here

num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
