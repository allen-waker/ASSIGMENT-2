#Write a Python function to insert a string in the middle of a string

def insert_string_middle(str, word):
    return str[:2] + word + str[2:]
print(insert_string_middle('[[]]','python'))
print(insert_string_middle('{{}}','php'))
print(insert_string_middle('<<>>','html'))