'''  - Modify program in S01Q02 to print the multiplication table using functions
           of any number desired by the user'''


def table():
    num = input("Enter the value of the desired table here:")
    i = 1

    while i <= 10:
        res = int(num) * i
        print( int(num)," x", i,"=",res)
        i = i + 1
#Main starts here

table()
