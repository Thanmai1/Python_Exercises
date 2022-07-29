'''Get the user’s first name and last name. 
        Assume the user provides “Dharmender” and “Singh” as inputs, 
          then print the user’s name in the following order and format

        - Name : dharmender, Surname : singh 
        - DHARMENDER SINGH
          ---------------------  ---------
        - Singh, Dharmender'''

first_name = input("Enter the first name:")
last_name = input("Enter the last name :")

a = first_name.lower()
b = last_name.lower()
A = first_name.upper()
B = last_name.upper()

print("- Name :",",", a, "Surname :", b)
print("-", A, B)
nf = len(first_name)
nl = len(last_name)
print("-"* nf, " ", "-"*nl )
print("-", last_name,",",first_name)

