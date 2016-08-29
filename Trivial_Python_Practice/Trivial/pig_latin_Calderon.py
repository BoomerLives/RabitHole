# Author: Nathan Calderon
# File Name: pig_latin_Calderon.py

# This program asks a user for a sentence and converts each word to "Pig Latin"

# Define main function.
def main():
    # Create string to concatenate.
    piglatin_sentence = " "
    # User enters a sentence to convert to piglating.
    sentence = input("Enter a sentence to convert to Pig Latin: ")
    # Sentence is split.
    sent = sentence.split()
    # For loop to convert each word and concatenate to new sentence. 
    for word in sent:
        piglatin_word = (word[1:] + word[0] + "ay" + " ")
        piglatin_sentence += piglatin_word
    # Line break
    print()
    # Force all letter to uppercase.
    piglatin_up = piglatin_sentence.upper()
    # Display pig latin sentence.
    print(piglatin_up)
    print()
    input("Press enter to continue...")

# Call main function.
main()


# Inputs: I like to code / I slept most of the night
# Outputs: IAY IKELAY OTAY ODECAY / IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY 
