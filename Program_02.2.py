# The taskS.
# Create a program that will cheack if password is valid.
# Password is valid if criteria is met.
# > 15 letters.
# Have atleast one capital letter.
# Have atleat one number.
# Have atleast one special character.


def inputed_password():
    # get the password combination
    combination = input("Enter a password: ")
    return combination


def verify_pass(key):
    lower = 0
    upper = 0
    special = 0
    digit = 0
    # check if the password is have 15 characters.
    if (len(key) >= 15):
        for mix in key:
            for word in key.split():
                # check is password have a uppercase letter.
                if(word[0].isupper()):
                    upper += 1
            # check is password have a lowercase letter.
            if(mix.islower()):
                lower += 1
            # check is password have a number.
            if(mix.isdigit()):
                digit += 1
            if(mix == '%' or mix == '?' or mix == '(' or mix == ')' or mix == ',' or mix == '~' or mix == '!' or mix == '^' or mix == '&' or mix == '/' or mix == '+' or mix == '>' or mix == '@' or mix == '$' or mix == '_' or mix == '#'):
                special += 1
    else:
        print("Password should atleast 15 or more combination")
    if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
        print("Valid Password")
    else:
        print("Invalid Password")


key = inputed_password()
verify_pass(key)
