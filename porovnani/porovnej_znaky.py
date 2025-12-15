from pathlib import Path

def load_tokens(path: str) -> list[str]:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    tokens = []
    for line in text.splitlines():
        for part in line.split(","):
            token = part.strip()
            if token != "":
                tokens.append(token)
    return tokens

# Načtení dat
tokens_a = load_tokens("A.txt")
tokens_b = load_tokens("B.txt")

set_b = set(tokens_b)

shody = 0
neshody = 0
vystup = []

vystup.append("=== VÝSLEDEK POROVNÁNÍ ===\n")

for token in tokens_a:
    if token in set_b:
        vystup.append(f"token se SHODUJE:    {token}")
        shody += 1
    else:
        vystup.append(f"token se NESHODUJE:  {token}")
        neshody += 1

vystup.append("\n=== SOUHRN ===")
vystup.append(f"Shod:     {shody}")
vystup.append(f"Neshod:   {neshody}")
vystup.append(f"Celkem A: {len(tokens_a)}")

# Zápis do souboru
Path("vysledek.txt").write_text("\n".join(vystup), encoding="utf-8")

print("Hotovo ✔ Výsledek je uložen v souboru: vysledek.txt")
