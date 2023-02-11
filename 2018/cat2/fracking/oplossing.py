def gaatInstorten(grond):
    for indexLaag, laag in enumerate(grond):
        laagGeconnecteerd = False
        for indexDeel, deel in enumerate(laag):
            verticaleLijnZachtRechts = indexDeel < len(
                laag)-1 and "*" not in [laag[indexDeel+1] for laag in grond]
            if deel == "*":
                grenstAan = grenstAanDeel(
                    grond, indexLaag, indexDeel, True, True)
                laagGeconnecteerd = grenstAan or laagGeconnecteerd
                if indexLaag == 0:
                    grenstAan = grenstAanDeel(
                        grond, indexLaag, indexDeel, True, False)
                    if grenstAan is False:
                        return True
                if verticaleLijnZachtRechts and laagGeconnecteerd is False:
                    return True

        if laagGeconnecteerd is False:
            return True
    return False


def grenstAanDeel(grond, indexLaag, indexKolom, isHard, enkelVerticaal):
    grenstAan = False
    teken = "*" if isHard else "."

    # boven
    if indexLaag != len(grond)-1:
        grenstAan = grond[indexLaag+1][indexKolom] == teken

    if enkelVerticaal and indexLaag != len(grond)-1:
        return grenstAan

    # onder
    if indexLaag != 0:
        grenstAan = grenstAan or grond[indexLaag-1][indexKolom] == teken

    if enkelVerticaal:
        return grenstAan

    # links
    if indexKolom != 0:
        grenstAan = grenstAan or grond[indexLaag][indexKolom-1] == teken

    # rechts
    if indexKolom != len(grond[0])-1:
        grenstAan = grenstAan or grond[indexLaag][indexKolom+1] == teken

    return grenstAan


aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    aantalDagen = 0
    aantalRijen = int(input())
    aantalKolommen = int(input())
    grond = []
    for a in range(aantalRijen):
        grond.append(list(input()))
    stortIn = gaatInstorten(grond)
    while stortIn is False:
        aantalDagen += 1
        nieuweGrond = [_[:] for _ in grond]
        for indexLaag, laag in enumerate(grond):
            for indexDeel, deel in enumerate(laag):
                if deel == "*" and grenstAanDeel(grond, indexLaag, indexDeel, False, False):
                    nieuweGrond[indexLaag][indexDeel] = "."
        grond = nieuweGrond
        stortIn = gaatInstorten(grond)

    print(f"{i + 1} {aantalDagen}")
