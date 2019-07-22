import timeit


start = timeit.default_timer()


# looks at a hash from the Credentials file and looks for a matching hash from hashed_dictionary file
# my haashed_dictionary file only contained the first 50 entries from the dictionary file
def compare_hashes():
    successful_crack = False
    with open("Credentials") as password_file:
        for line in password_file:
            stored_username, stored_password = line.split(":")
            stored_password = stored_password.rstrip("\n")
            with open("hashed_dictionary") as dictionary:
                for line in dictionary:
                    pw_plaintext, pw_hash = line.split(":")
                    pw_hash = pw_hash.rstrip("\n")
                    if pw_hash == stored_password:
                        stop = timeit.default_timer()
                        print("Found a match!")
                        print("Username: " + stored_username)
                        print("Password" + ": " + pw_plaintext)
                        print("Runtime: ", stop - start)
                        successful_crack = True
                        input("Press Enter key to exit.")
                        break
    return successful_crack


found_password = compare_hashes()


# will only run code if the first function didn't produce a result
def compare_hashes_type2(found_password):
    if found_password is False:
        with open("Credentials") as password_file:
            for line in password_file:
                stored_username, stored_password = line.split(":")
                stored_password = stored_password.rstrip("\n")
                with open("hashed_dictionary_type2") as dictionary:
                    for line in dictionary:
                        pw_plaintext, pw_hash = line.split(":")
                        pw_hash = pw_hash.rstrip("\n")
                        if pw_hash == stored_password:
                            stop = timeit.default_timer()
                            print("Found a match!")
                            print("Username: " + stored_username)
                            print("Password" + ": " + pw_plaintext)
                            print("Runtime: ", stop - start)
                            input("Press Enter key to exit.")
                            break


compare_hashes_type2(found_password)
