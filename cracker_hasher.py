import hashlib

# The function call for the second function is currently commented out

special_chars = ["!", "@", "#", "$", "%", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# converts the lines from the dictionary file to hashes
# stores those hashes in file hashed_dictionary along with their plaintext version
# takes a really long time, not recommended to attempt the whole dictionary
# personally only hashed the first 50 entries
def hash_dictionary():
    with open("test_dictionary.txt") as dictionary:
            for line in dictionary:
                password_plaintext = line.rstrip("\n")
                password_encoded = password_plaintext.encode('utf-8')
                m = hashlib.md5(password_encoded)
                password_hash = m.hexdigest()
                hashed_dictionary_file = open("hashed_dictionary", "a")
                hashed_dictionary_file.write(password_plaintext + ":" + password_hash + "\n")
                print(password_plaintext)


# takes the plaintexts from previous function and adds special characters
# adds new type2 passwords to an array
# hashes everything in the array and appends to file hashed_dictionary_type2
# not recommended to allow this function to attempt more than a couple dozen or so dictionary entries
def hash_dictionary_type2():
    type2_passwords = []
    with open("hashed_dictionary") as dictionary:
        for line in dictionary:
            password_plaintext, ignorable_hash = line.split(":")

            for x in special_chars:
                # adds special character to beginning of entry
                # adds new type2 to an array
                new_type2 = x + password_plaintext
                print(new_type2)
                type2_passwords.append(new_type2)
                # adds special character to end
                new_type2 = password_plaintext + x
                print(new_type2)
                type2_passwords.append(new_type2)
        # takes previously made type2s and adds more special characters
        for y in type2_passwords:
            more_type2s = []
            for x in special_chars:
                # adds another special character to end
                new_type2 = y + x
                print(new_type2)
                more_type2s.append(new_type2)
            for x in special_chars:
                # adds another special character to beginning
                new_type2 = x + y
                print(new_type2)
                more_type2s.append(new_type2)
            # adds these type 2s to original type 2 array
            type2_passwords = type2_passwords + more_type2s

        # hashes all from the type2 array and appends to hashed_dictionary_type2
        for x in type2_passwords:
            password_encoded = x.encode('utf-8')
            m = hashlib.md5(password_encoded)
            password_hash = m.hexdigest()
            hashed_dictionary_file = open("hashed_dictionary_type2", "a")
            hashed_dictionary_file.write(x + ":" + password_hash + "\n")


hash_dictionary()
#hash_dictionary_type2()
