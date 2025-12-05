## Pouziti RE knihovny 

---

## ✨ Obecne

Modul `re` je jeden z nejdůležitějších nástrojů pro Python automatizaci.
Umožní ti rychle a přesně zpracovávat textová data, validovat vstupy a extrahovat hodnoty z logů či konfiguračních souborů.

---

### pouziti 

* parsování logů
* extrakce dat
* validace vstupů
* scraping
* filtrování textů
* práce s konfiguráky
* automatické úpravy souborů
* detekce vzorů
* automatizované rename operace

**Regex = základní nástroj automatizátora.**



---


## 🔹 Modul `re` – regulární výrazy v Pythonu

Modul `re` poskytuje práci s regulárními výrazy, což jsou vzory pro vyhledávání, filtrování a manipulaci s textem.
V automatizaci se používají při extrakci dat, parsování logů, validaci vstupů nebo úpravách konfiguračních souborů.

### 👉 Načtení modulu

```python
import re
```

---

## 🔹 Základní funkce

### `re.search(pattern, string)`

Najde **první výskyt** vzoru kdekoli v textu.

```python
m = re.search(r"\d+", "ID: 123")
print(m.group())  # 123
```

### `re.findall(pattern, string)`

Vrátí **všechny shody** jako list.

```python
re.findall(r"\d+", "10 20 30")  
# ['10', '20', '30']
```

### `re.sub(pattern, replacement, string)`

Nahradí všechny výskyty vzoru.

```python
re.sub(r"\s+", "_", "hello world test")
# 'hello_world_test'
```

### `re.split(pattern, string)`

Rozdělí text podle vzoru.

```python
re.split(r"[,;]+", "a,b;c")
# ['a', 'b', 'c']
```

---

## 🔹 Základní syntax vzorů (regex)

| Vzor    | Význam             |
| ------- | ------------------ |
| `.`     | libovolný znak     |
| `\d`    | číslice            |
| `\w`    | alfanumerický znak |
| `\s`    | whitespace         |
| `+`     | jeden nebo více    |
| `*`     | nula nebo více     |
| `?`     | nula nebo jeden    |
| `{m,n}` | interval výskytů   |
| `^`     | začátek řetězce    |
| `$`     | konec řetězce      |

---

## 🔹 Skupiny (groups)

Pomocí závorek lze vytáhnout části textu:

```python
m = re.search(r"(\d+)\s+(\w+)", "10 apples")
print(m.group(1))  # 10
print(m.group(2))  # apples
```

---

## 🔹 Flagy (přepínače)

```python
re.IGNORECASE   # ignoruje velikost písmen
re.MULTILINE    # ^ a $ fungují na každý řádek
re.DOTALL       # tečka matchuje i \n
```

Příklad:

```python
re.search(r"python", "PYTHON", re.IGNORECASE)
```

---

## 🔹 Praktické příklady pro automatizaci

### Extrakce všech čísel

```python
numbers = re.findall(r"\d+", text)
```

### Validace e-mailu

```python
re.fullmatch(r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email)
```

### Odstranění všech speciálních znaků

```python
clean = re.sub(r"[^a-zA-Z0-9 ]", "", text)
```

### Parsování logu

```python
match = re.search(r"ERROR (\d+): (.*)", line)
if match:
    code = match.group(1)
    message = match.group(2)
```


# ⭐ 1) Najít první výskyt vzoru (`re.search`)

```python
import re

text = "Objednavka cislo 984 byla prijata."

match = re.search(r"\d+", text)
if match:
    print("Nalezeno číslo:", match.group())
```

➡️ Výsledek: `984`

---

# ⭐ 2) Najít všechna čísla (`re.findall`)

```python
import re

text = "Ceny: 150, 299, 450."

numbers = re.findall(r"\d+", text)
print(numbers)
```

➡️ `['150', '299', '450']`

---

# ⭐ 3) Validovat formát e-mailu (`re.fullmatch`)

```python
email = "user.name@example.com"

if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Email OK")
else:
    print("Neplatny email")
```

---

# ⭐ 4) Nahradit mezery podtržítky (`re.sub`)

```python
text = "ahoj jak se mas"
converted = re.sub(r"\s+", "_", text)

print(converted)
```

➡️ `ahoj_jak_se_mas`

---

# ⭐ 5) Rozdělit text podle více oddělovačů (`re.split`)

```python
text = "jablko;hruska,merunka|kiwi"
parts = re.split(r"[;,|]", text)

print(parts)
```

➡️ `['jablko', 'hruska', 'merunka', 'kiwi']`

---

# ⭐ 6) Extrakce hodnot z logu (super pro automatizaci)

```python
log = "ERROR 500: Internal server failure at 12:45"

match = re.search(r"ERROR (\d+): (.+)", log)
if match:
    code = match.group(1)
    message = match.group(2)

    print("Kód chyby:", code)
    print("Zpráva:", message)
```

---

# ⭐ 7) Najít telefonní čísla

```python
text = "Moje cisla: +420777888999 a 603123456."

phones = re.findall(r"\+?\d{9,12}", text)
print(phones)
```

---

# ⭐ 8) Odstranit všechny speciální znaky

```python
text = "Nazev@Souboru#$%.txt"
clean = re.sub(r"[^a-zA-Z0-9._-]", "", text)

print(clean)
```

➡️ `NazevSouboru.txt`

---

# ⭐ 9) Získat hodnotu z konfiguráku

```python
config = "timeout=1500ms"

match = re.search(r"timeout=(\d+)ms", config)
if match:
    timeout_value = int(match.group(1))
    print("timeout:", timeout_value)
```

---

# ⭐ 10) Zachytit skupiny (multiple groups)

```python
text = "Jmeno: Jan | Vek: 34 | Mesto: Brno"

match = re.search(r"Jmeno:\s*(\w+).*Vek:\s*(\d+).*Mesto:\s*(\w+)", text)

if match:
    name = match.group(1)
    age  = match.group(2)
    city = match.group(3)

    print(name, age, city)
```

---

# ⭐ 11) Použití `re.compile()` pro rychlost (pokročilé)

Pokud regex používáš opakovaně:

```python
pattern = re.compile(r"\d{3}-\d{2}-\d{4}")

for line in data:
    if pattern.search(line):
        print("Nalezen vzor:", line)
```

---

# ⭐ 12) Negativní lookahead (pokročilý příklad)

Najdi číslo, které **není** následováno slovem „kg“.

```python
re.findall(r"\d+(?!\s*kg)", "10 kg, 20, 30 kg, 40")
```

➡️ `['20', '40']`

---






