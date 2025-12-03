import re

# IPv4 adresa s VOLITELNOU maskou /XX
# - teď ale do množiny ukládáme CELÝ řetězec, včetně prefixu
ip_regex = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?\b')

def extract_ip_prefixes(path):
    ips = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for match in ip_regex.findall(line):
                ips.add(match.strip())
    return ips

file_a = "souborA.txt"   # IP/prefixy, které MUSÍ být obsažené
file_b = "souborB.txt"   # kde kontrolujeme, jestli tam jsou

ips_a = extract_ip_prefixes(file_a)
ips_b = extract_ip_prefixes(file_b)

missing = sorted(ips_a - ips_b)

print(f"Počet unikátních IP/prefixů v A: {len(ips_a)}")
print(f"Počet unikátních IP/prefixů v B: {len(ips_b)}")

if not missing:
    print("\n✅ OK: Soubor B obsahuje všechny IP/prefixy ze souboru A.")
else:
    print("\n❌ Tyhle IP/prefixy jsou v A, ale chybí v B:")
    for ip in missing:
        print(ip)
    with open("chybi_ip.txt", "w", encoding="utf-8") as f:
        for ip in missing:
            f.write(ip + "\n")
    print('\nSeznam chybějících IP/prefixů je uložen v "chybi_ip.txt".')
