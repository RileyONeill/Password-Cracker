import hashlib

# prompts user for their login credentials, hashes the password, and runs them through the validator
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    password_hash = password_hasher(password)
    validate_login(username, password_hash)


def validate_login(username, password_hash):
    with open("Credentials") as f:
        found_username = False
        # looks through Credentials file to find a line that begins with the inputted username
        for line in f:
            stored_username, stored_password = line.split(":")
            #this line strips the \n from the read line
            stored_password = stored_password.rstrip("\n")
            if username == stored_username:
                found_username = True
                if stored_password == password_hash:
                    print("Successful login!")
                    input("Press Enter key to exit.")
                else:
                    print("Invalid username or password.")
                    login()
        if found_username is False:
            print("Invalid username or password.")
            login()


# converts inputted password to a hash
def password_hasher(password):
    password_encoded = password.encode('utf-8')
    m = hashlib.md5(password_encoded)
    password_hash = m.hexdigest()
    return password_hash


login()
