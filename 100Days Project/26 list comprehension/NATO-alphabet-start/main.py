import pandas


def generate_phonetic():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    user_input = input("Enter a word: ").upper()

    try:
        phonetic_code = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()
