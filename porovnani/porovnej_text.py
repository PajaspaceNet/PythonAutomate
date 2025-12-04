def load_list(path):
    """Načte textový soubor, odstraní prázdné řádky a mezery okolo textu.
       Vrací množinu hodnot (unikátní řádky)."""
    with open(path, "r", encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}


file_a = "souborA.txt"  # hodnoty, které MUSÍ být obsaženy
file_b = "souborB.txt"  # kde hledáme

setA = load_list(file_a)
setB = load_list(file_b)

# řádky, které jsou v A, ale nejsou v B
missing = sorted(setA - setB)

print("Počet hodnot v A:", len(setA))
print("Počet hodnot v B:", len(setB))

if not missing:
    print("\n✅ Ve sloupci B NECHYBÍ žádná hodnota ze sloupce A.")
else:
    print("\n❌ Ve sloupci B chybí tyto hodnoty:")
    for m in missing:
        print(m)

    # uložit výsledek do souboru
    with open("chybi.txt", "w", encoding="utf-8") as f:
        for m in missing:
            f.write(m + "\n")

    print('\nVýsledek uložen do souboru "chybi.txt".')
