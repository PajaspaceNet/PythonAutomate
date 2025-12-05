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





