names_list = []

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names_list:
        stripped_name = name.strip()
        letter_content.replace('[name]', stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(letter_content)