
'''Get the user’s first name and last name. 
        Assume the user provides “Dharmender” and “Singh” as inputs, 
        Find his best possible initials by eliminating the last character 
        from each of the name as shown in this sample output

        - Step 1 : Dharmender Singh
        - Step 2 : Dharmende Sing
        - Step 3 : Dharmend Sin
        - Step 4 : Dharmen Si
        - Step 5 : Dharme S

        Expected output :
        Best possible initials of "Dharmender Singh" is :
        Dharme S'''

first_name = input("Enter the first name:")
last_name = input("Enter the last name :")
nf = len(first_name)
nl = len(last_name)
i=0
while i< nl - 1:
    first_name = first_name[:-1]
    last_name = last_name[:-1]
    i=i+1

print(" Best possible initials of is:")
print(first_name , last_name)
