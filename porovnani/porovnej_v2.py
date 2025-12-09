def load_list(path):
    """Načte textový soubor, odstraní prázdné řádky a mezery kolem textu.
    Vrací množinu hodnot ( unikátní řádky )."""
    with open(path, "r", encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}


file_a = "soubor_text_A.txt"  # hodnoty, které MUSÍ být obsaženy v B
file_b = "soubor_text_B.txt"  # kde hledáme

setA = load_list(file_a)
setB = load_list(file_b)

# řádky, které jsou v A, ale nejsou v B
missing = sorted(setA - setB)

# řádky, které jsou v B, ale nejsou v A
extra_in_B = sorted(setB - setA)

print("Počet hodnot v A:", len(setA))
print("Počet hodnot v B:", len(setB))

if not missing and not extra_in_B:
    print("\n✅ Žádné rozdíly mezi A a B.")
else:
    if missing:
        print("\n❌ Ve sloupci B chybí tyto hodnoty ze sloupce A:")
        for m in missing:
            print(m)
    if extra_in_B:
        print("\n❗️ Hodnoty v B, které ani nebyly zadany ale mely byt v A:")
        for e in extra_in_B:
            print(e)

# Uložit výsledek do souboru (původní chyba)
with open("chybi.txt", "w", encoding="utf-8") as f:
    for m in missing:
        f.write(m + "\n")

# Uložit dodatečné rozdíly (extra_in_B) do souboru
with open("navic_v_B_nev_A.txt", "w", encoding="utf-8") as f:
    for e in extra_in_B:
        f.write(e + "\n")

print('\nVýsledek uložen do souborů "chybi.txt" a "navic_v_B_nev_A.txt".')
