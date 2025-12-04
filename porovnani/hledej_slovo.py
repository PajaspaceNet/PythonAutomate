def find_lines_with_word(path, word):
    word = word.lower()  # case-insensitive
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if word in line.lower():
                print(line.strip())


# nastavení
filename = "soubor.txt"
search_word = "heslo"   # sem dej slovo, které hledáš

print(f"Hledám řádky obsahující: '{search_word}'\n")
find_lines_with_word(filename, search_word)
