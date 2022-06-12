'''Modify the first “Hello World” program to prompt for user’s name 
           and then wish the user by saying Hello followed by his name

           Example :
           If user's name is Sam, then expected output is :
           Hello Sam !!!'''

def hello():
    name = input("Enter your name here:")
    print("Hello", name)


#main starts here
hello()
