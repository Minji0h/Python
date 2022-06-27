PLACEHOLDER = "[name]"
INVITED_NAMES_FILE = "Input/Names/invited_names.txt"
STARTING_LETTER_FILE = "Input/Letters/starting_letter.txt"

#Faz a leitura do arquivo com os nomes dos convidados
with open(INVITED_NAMES_FILE, 'r') as name_file:
    names = name_file.readlines()
    name_file.close()
    

with open(STARTING_LETTER_FILE,'r') as letter_file:
    letter_contents = letter_file.read()
    letter_file.close()

for name in names:
    name = name.strip()
    new_letter = letter_contents
    new_letter = new_letter.replace(f"{PLACEHOLDER}",f"{name}")
    with open(f"Output\ReadyToSend/letter_for_{name}.txt", "a") as letter_final:
        letter_final.write(f"{new_letter}")
        letter_final.close()
