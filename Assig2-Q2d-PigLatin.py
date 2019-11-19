#
'''Write a program that will take a word and output the pig latin version of the word
by following the following rules:
1. If the word starts with a consonant or group of consonants, move all letters
before the first vowel to the end of the word then add "ay".
2. If the word starts with a vowel, simply add "way" to the end of the word.'''

mystring=input("Enter a String to Translate: ")
vowels="aeiou"

# First, pick the first letter and check if its a vowel
mfirst=mystring[0:1]
if (mfirst.upper() in vowels.upper()):  # First letter is a vowel
  mystring=mystring+"way"     # Just add way at the end
  print(mystring)
else:                   # First letter is a consonant
  counter=0        # start scanning thru the string
  while counter<len(mystring):   # Until end of string
    letter=mystring[counter:counter+1]        # Pick next letter
    if (letter.upper() in vowels.upper()):    # Check if its a vowel
      #print(letter,counter, len(mystring))
      mword=mystring[counter:len(mystring)]   # Slice the string at this point
      mconsonants=mystring[0:counter]         # Pick the initial consonants
      #print (mword,mconsonants)
      mword=mword+mconsonants+"ay"            # Arrange the new word
      print(mword)                            # Output this new word
      counter=len(mystring)+1       # Force an exit from the loop
    counter += 1

