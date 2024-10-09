from textblob import TextBlob

text = input("Enter the text: ")
text = TextBlob(text)
print("The corrected text is: ", text.correct())

