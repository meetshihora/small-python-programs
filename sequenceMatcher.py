from difflib import SequenceMatcher

frist_sentence = input("Enter your frist sentence: ")
second_sentence = input("Enter your second sentence: ")

print((SequenceMatcher(None, frist_sentence, second_sentence).ratio()*100))