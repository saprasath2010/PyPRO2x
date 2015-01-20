words = open("spell.words.txt").readlines()
words = dict(map(lambda x: x.strip(), words))

print(type(words))
if 'are' in words:
    print("Yeah found the value")
