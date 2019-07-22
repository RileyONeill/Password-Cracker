import hashlib


def new_user():
    new_username = input("Enter a username: ")
    if check_username(new_username):
        password_plaintext = input("Enter a password: ")
        valid_username = check_username(new_username)
        # turns plaintext into hashable format
        password_encoded = password_plaintext.encode('utf-8')

        # runs input through md5
        m = hashlib.md5(password_encoded)

        # turns hash into readable hexadecimal format
        password_hash = m.hexdigest()
        # appends username and password hash to a file titled Credentials in the format 'username:password'
        f = open("Credentials", "a")
        f.write(new_username + ":" + password_hash + "\n")
        print("New user successfully created.")
        input("Press Enter key to exit.")
    if check_username(new_username) is False:
        print("Username already taken.")
        new_user()


# this function makes sure the username isn't already taken
def check_username(new_username):
    valid_username = True
    with open("Credentials") as f:
        for line in f:
            # credentials are stored in format 'username:password', these lines takes out just the username
            file_line = line.split(":")
            existing_username = file_line[0]
            if new_username == existing_username:
                valid_username = False
                break
    return valid_username


new_user()
