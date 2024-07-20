# ask the user to enter a sentence and a word to replace, then the new word. Replace the old word with the new word in the sentence.

sentence = input("Enter a sentence:")
a=input("Enter a word to replace in that sentence:")
b=input("Enter the word you want to replace it with:")

print("replacing sentence...")
print(sentence.replace(a,b))
