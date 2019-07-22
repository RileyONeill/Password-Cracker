

# uses escalating series of booleans to see which criteria a user's password meets
def evaluator():
    password = input("Enter a password: ")
    weak = False
    moderate = False
    with open("dictionary.txt") as dictionary:
        for line in dictionary:
            dictionary_entry = line.rstrip("\n")
            # weak is true if password exactly matches a dictionary entry
            if password == dictionary_entry and len(dictionary_entry) > 2:
                weak = True
            # without this line, a password shorter than any dictionary entry would be considered strong
            if len(password) < 8:
                weak = True
            # if password was not weak but does contain dictionary entry as a substring, moderate is true
            elif dictionary_entry in password and len(dictionary_entry) > 2:
                moderate = True
        # if there was an exact dictionary match, immediately evaluate it as weak
        if weak is True:
            print("This is a weak password.")
            evaluator()
        # if weak was false but moderate true, then it's moderate.
        elif moderate is True:
            print("This is a moderate password.")
            evaluator()
        # otherwise it must be strong
        else:
            print("This is a strong password.")
            evaluator()


evaluator()
