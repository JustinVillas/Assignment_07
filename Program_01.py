# Task
# Create a program that ask for a sentence input
# Display the number of words, vowels and consonants in the input

def inputed_senc():
    senc = input("Construct a senctence: ")
    return senc


def count_letters(cons_senc):
    vowels = 0
    consonants = 0

    for letters in range(0, len(cons_senc)):

        char = cons_senc[letters]

        if ((char >= 'a' and char <= 'z') or
                (char >= 'A' and char <= 'Z')):

            char = char.lower()
            if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
                vowels += 1
            else:
                consonants += 1

    print(f"Vowels = {vowels}")
    print(f"Consonant = {consonants}")


def count_word(cons_senc):
    a_string = cons_senc
    word_list = a_string.split()
    number_of_words = len(word_list)
    print(f"Words = {number_of_words}")


cons_senc = inputed_senc()
count_letters(cons_senc)
count_word(cons_senc)
