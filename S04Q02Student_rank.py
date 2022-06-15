''' Brilliant School sets an exam wherein, 
                English exam is for 80 marks, 
                Science for 90 marks and 
                Mathematics for 100 marks. 

            Ask the student to enter the marks scored in each of these exams. 
            Calculate the total percentage marks and rank the student as below :
               - First Class if score is more than or equal to 90 %
               - Second Class if score is more than or equal to 75%
               - Average if student has not failed
               - Failed if score is less than or equal to 35 %

            Make sure your code uses the same principles 
                 as in the template codes of earlier exercises
'''

def get_studentmarks():
    E = input("Enter your English score:")
    S = input("Enter your Science score:")
    M = input("Enter your Math score:")
    max_total = 270
    total = int(E)+int(S)+int(M)
    percentage = (int(total)/int(max_total))*100

    return(percentage)

def student_rank(percentage):

    if percentage >= 90:
        print(" You passed in first class!")
    if percentage >= 75 and percentage <90:
        print("You passed in Second class!")
    if percentage > 35 and percentage <75:
        print("Your score is Average!")
    if percentage <= 35:
        print(" You have failed!")

student_rank(get_studentmarks())
