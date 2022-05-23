''' - Modify program in S01Q02 to print the multiplication table 
           of any number desired by the user'''


table = input("Enter the multiplication table number:")

i = 1
while i <= 10:
    res = int(table) *i
    print( table , "x",i,"=",res )
    i = i + 1
