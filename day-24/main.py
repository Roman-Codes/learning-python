PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as template:
    template_contents = template.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = template_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", "w") as letters:
            letters.write(new_letter)
