''' - Ask the user to enter a number.
     - If the number is a single digit number,
         add 7 to it, and print the number in its unit’s place
     - If the number is a two digit number,
        raise the number to the power of 5, 
            and print the number in its unit’s place
      - If the number is a three digit number, 
           ask the user to enter another number. 
          Add the 2 numbers and print the number in its unit’s place

      Use the solution provided in S03Q01 as the template for this exercises.
  - Instead of doing a print to print the final result in "perform_check" function 
         call separate functions : 
               do_1digit_oper() and
               do_2digit_oper() and
               do_3digit_oper()
     that will perform the required operations based on the number of digits.
'''

def get_number():
    num = input("Enter the number here:")
    return (int(num))

def perform_check(number):
    if number <= 9:
        do_1digit_oper(number)
    if number >9 and number <= 99:
        do_2digit_oper(number)
    if number >99 and number <= 999:
        do_3digit_oper(number)

def do_1digit_oper(num):
    a = num+7
    b = a%10
    print(" the units place is:" ,(int (b)))
def do_2digit_oper(num):
    a = num**5
    b = a%10
    print(" It is a 2 - digit number and its units place is ", int(b))

def do_3digit_oper(num):
    num2 = input("enter another number here:")
    a = int(num2) + int(num)
    b = a%10
    print("The units place is :", int(b))

#main starts here

num1 = get_number()

perform_check(num1)
