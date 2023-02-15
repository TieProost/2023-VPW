def min_rekken(boeken, rekken):

    if (len(boeken) == 0):
        return 0

    if (len(rekken) == 0):
        return "ONMOGELIJK"

    rek_i = 0
    for boek in boeken:
        breedte = int(boek.split(',')[1])

        while rek_i < len(rekken) - 1 and int(rekken[rek_i]) < breedte:
            rek_i += 1

        if int(rekken[rek_i]) >= breedte:
            rekken[rek_i] = rekken[rek_i] - breedte
        else:
            return "ONMOGELIJK"

    return rek_i+1


for i in range(int(input())):

    rekken = input().split(" ")[1:]
    rekken = [int(x) for x in rekken]
    rekken.sort()
    rekken.reverse()

    boeken = []
    for j in range(int(input())):
        nieuw_boek = input().split(" ")
        boeken += [f"{nieuw_boek[1]},{nieuw_boek[0]}"]
    boeken.sort()

    print(i+1, min_rekken(boeken, rekken))
