import pandas

DATA = "nato_phonetic_alphabet.csv"

phonetic_alphabet = pandas.read_csv(DATA)
phonetic_dict = {row.letter:row.code for (index,row) in phonetic_alphabet.iterrows()}

word = input("Enter a word: \n").upper()

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
