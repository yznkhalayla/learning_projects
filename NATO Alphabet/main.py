import pandas


def NATO():

    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    NATO_df = pandas.DataFrame(data)

    NATO_dict = {row.letter:row.code for (index, row) in NATO_df.iterrows()}

    word = input().upper()

    try:
        # new_NATO = [value for (key, value) in NATO_dict.items() if key in word]
        new_NATO = [NATO_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the Alphabet please.\nEnter a word:")
        NATO()
    else:
        print(new_NATO)


NATO()
