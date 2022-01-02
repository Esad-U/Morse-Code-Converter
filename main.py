from Morse import *

if __name__ == '__main__':
    sentence = input("Enter the sentence to be converted (all lower case, no punctuation): ")
    converter = Morse()
    print(converter.convert_to_morsecode(sentence))
