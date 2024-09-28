def character_count(sentance):
    count = {}
    for i in sentance:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

text = input("Enter your text: ")
character_count(text)