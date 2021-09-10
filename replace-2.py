import codecs

non_ascii_characters = set()

with open('hello.txt') as file:
    i = 0
    for line in file:
        print(i)
        i += 1
        for c in line:
            if not (0 <= ord(c) <= 127):
                non_ascii_characters.add(c)

f = codecs.open("hello.txt", encoding='utf-8')
contents = f.read()

search_array = list(non_ascii_characters)
replace_array = []
for non_ascii_character in search_array:
    replace_array.append(non_ascii_character.encode("unicode_escape").decode("utf-8")[1:])

trans = str.maketrans(dict(zip(search_array, replace_array)))

cleaned = contents.translate(trans)

f = open("hello-update.txt", "w")
f.write(cleaned)
f.close()


dictionary = dict(zip(search_array, replace_array))
print(dictionary)