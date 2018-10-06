import ftfy

with open("data/small_text.json") as fp:
    for line in fp:
        print(ftfy.fix_encoding(line), end='')
