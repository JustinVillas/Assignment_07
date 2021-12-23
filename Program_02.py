# The task
# Create a program that will cheack if password is valid
# Password is valid if criteria is met.
# > 15 letters
# Have atleast one capital letter.
# Have atleast one number.
# Have atleast one special character.


def inputed_password():
    print(f"Hello user please follow the given instructions bellow.")
    print(f"Input 15 characters in your password.")
    print(f"Input atleast one UPPERCASE and a special character.")
    print(f"Input atleast one number.")
    print(f"------------------------------------------------------------------")
    combination = input("Enter a password: ")
    return combination


def check_password(key):
    special_sym = ["!", "@", "#", "%", "~", "$", "^", "&", "*", "(", ")", "_", "+"]
    val = True

    if len(key) > 15:
        if any(char.isdigit() for char in key):
            if any(char.upper() for char in key):
                if any(char.lower() for char in key):
                    if any(char in special_sym for char in key):
                        val = True
                        print(f"The password is valid")

    else:
        if len(key) <= 15:
            if not any(char.isdigit() for char in key):
                if not any(char.upper() for char in key):
                    if not any(char.lower() for char in key):
                        if not any(char in special_sym for char in key):
                            val = False
                            print(f"The password is not valid")


key = inputed_password()
check_password(key)
