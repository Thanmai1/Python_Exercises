'''Prompt the user to enter a long sentence
        - What is the last character in the sentence ?
        - What are the last 5 characters in the sentence ?
        - Print the characters that are present in 2nd and 5th position of the sentence
        - Print the character at the center of the string, along with the 2 adjoining characters. 
        Ex : If the string entered is "Web Browser”
        the character at its centre is "r" and so print "Bro"'''

long_sent = input("Enter a sentence:")
last_char = long_sent[-1:]
print(" Last character of the sentence is:", last_char)
last_five = long_sent[-5:]
print(" The last five characters of the sentence are:", last_five)
print("Character in 2nd position is:", long_sent[1])
print("Character in 5th position is:", long_sent[4])
len_sent = len(long_sent)
if (len_sent%2 != 0):
    d = int(len_sent/2)
    c = long_sent[d-1:d+2]
    print("The characters at the center of the string are:", c)
else:
    print("There is no center of the string")



