import constants
name = input("Enter your name please: ")
age = input("Enter your age: ")
print("{}, {} welcome to my code {}".format(name, constants.DATA_1, age))

string_data = r"""
This a multiline \n
string with escape sequences \n
Notice using raw string 
\t 
it prints the escape sequences as they are characters.
funny !!
"""

print(string_data)

