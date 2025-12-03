import re

ip_regex = re.compile(r'\b((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?\b')

def extract_ips(path):
    ips = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for ip in ip_regex.findall(line):
                ips.add(ip)
    return ips

file_a = "souborA.txt"
file_b = "souborB.txt"

ips_a = extract_ips(file_a)
ips_b = extract_ips(file_b)

missing = sorted(ips_a - ips_b)

print(f"Počet unikátních IP v A: {len(ips_a)}")
print(f"Počet unikátních IP v B: {len(ips_b)}")

if not missing:
    print("\n✅ OK: Soubor B obsahuje všechny IP adresy ze souboru A.")
else:
    print("\n❌ Tyhle IP jsou v A, ale chybí v B:")
    for ip in missing:
        print(ip)
    # uložíme do souboru, ať to máš na poslání
    with open("chybi_ip.txt", "w", encoding="utf-8") as f:
        for ip in missing:
            f.write(ip + "\n")
    print('\nSeznam chybějících IP je uložen v souboru "chybi_ip.txt".')
