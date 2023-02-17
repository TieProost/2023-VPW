def geefBuren(letter, landkaart, x, y):
    buren = []
    # boven
    if y != 0:
        buren.append(landkaart[y-1][x])
    # onder
    if y != hoogte-1:
        buren.append(landkaart[y+1][x])
    # links
    if x != 0:
        buren.append(landkaart[y][x-1])
    # rechts
    if x != breedte-1:
        buren.append(landkaart[y][x+1])

    return set(filter(lambda l: l != letter, buren))

aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    breedte, hoogte = (int(s) for s in input().split(" "))
    landkaart = [list(input()) for _ in range(hoogte)]

    dictBuren = {}
    for y in range(hoogte):
        for x in range(breedte):
            letter = landkaart[y][x]
            if dictBuren.get(letter) is None:
                dictBuren[letter] = set()
            dictBuren[letter] |= geefBuren(letter, landkaart, x, y)
    
    for rij in landkaart:
        cijfers = " ".join([str(len(dictBuren[l])) for l in rij])
        print(f"{i+1} {cijfers}")