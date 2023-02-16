import copy

def gaatInstorten(grond):
    if "*" not in grond[0] or "*" not in grond[aantalRijen-1]:
        return True
    else:
        ondersteLaag = [(aantalRijen-1, i) for i in range(0,aantalKolommen) if grond[aantalRijen-1][i] == "*"]
        bovensteLaag = [(0,i) for i in range(0, aantalKolommen) if grond[0][i] == "*"]
        
        closed = set()
        Q = []
        Q.extend(ondersteLaag)

        while len(Q) != 0:
            v = Q.pop(0)
            closed.add(v)
            for rijKolom in geefBuren(grond,v):
                if rijKolom in bovensteLaag:
                        return False
                elif rijKolom not in closed and rijKolom not in Q:
                    Q.append(rijKolom)
        return True

def geefBuren(grond, rijKolom):
    rij, kolom = rijKolom
    buren = []

    # onder
    if rij != aantalRijen-1 and grond[rij+1][kolom] == "*":
        buren.insert(0, (rij+1, kolom)) 

    # boven
    if rij != 0 and grond[rij-1][kolom] == "*":
        buren.insert(0, (rij-1, kolom))

    # links
    if kolom != 0 and grond[rij][kolom-1] == "*":
        buren.insert(0, (rij, kolom-1))

    # rechts
    if kolom != aantalKolommen-1 and grond[rij][kolom+1] == "*":
        buren.insert(0, (rij, kolom+1))
    
    return buren
    

def grenstAanZachtDeel(grond, indexLaag, indexKolom):
    grenstAan = False

    # onder
    if indexLaag != 0:
        grenstAan = grenstAan or grond[indexLaag-1][indexKolom] == "."

    # boven
    if indexLaag != aantalRijen-1:
        grenstAan = grenstAan  or grond[indexLaag+1][indexKolom] == "."

    # links
    if indexKolom != 0:
        grenstAan = grenstAan or grond[indexLaag][indexKolom-1] == "."

    #rechts
    if indexKolom != aantalKolommen-1:
        grenstAan = grenstAan or grond[indexLaag][indexKolom+1] == "."
    
    return grenstAan


aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    aantalRijen = int(input())
    aantalKolommen = int(input())
    grond = [list(input()) for a in range(aantalRijen)]

    aantalDagen = 0
    isIngestort = gaatInstorten(grond)

    while isIngestort is False:
        aantalDagen += 1
        nieuweGrond = copy.deepcopy(grond)
        for indexLaag, laag in enumerate(grond):
            for indexDeel, deel in enumerate(laag):
                if deel == "*" and grenstAanZachtDeel(grond,indexLaag, indexDeel):
                    nieuweGrond[indexLaag][indexDeel] = "."

        grond = nieuweGrond
        isIngestort = gaatInstorten(grond)

    print(f"{i + 1} {aantalDagen}")
    




