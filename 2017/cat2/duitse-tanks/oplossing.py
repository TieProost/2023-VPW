aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    getallen = []
    getal = int(input())
    while getal >= 0:
        getallen.append(getal)
        getal = int(input())
    
    m = max(getallen)
    n = len(getallen)
    t = round(((n + 1) * m ) / n - 1)
    print(f"{i+1} {t}")