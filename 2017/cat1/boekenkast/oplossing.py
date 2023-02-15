def min_rekken(boeken, rekken):
    rekken = [int(x) for x in rekken]
    rekken.sort()
    rekken.reverse()
    boeken.sort()

    if (len(boeken) == 0):
        return 0

    if (len(rekken) == 0):
        return "ONMOGELIJK"

    i_rek = 0
    for boek in boeken:
        while i_rek < len(rekken) - 1 and int(rekken[i_rek]) < int(boek.split(',')[1]):
            i_rek += 1
        if int(rekken[i_rek]) >= int(boek.split(',')[1]):
            rekken[i_rek] = rekken[i_rek] - int(boek.split(',')[1])
        else:
            return "ONMOGELIJK"

    return i_rek+1


for i in range(int(input())):
    boeken = []
    rekken = input().split(" ")[1:]

    for j in range(int(input())):
        nieuw_boek = input().split(" ")
        boeken += [f"{nieuw_boek[1]},{nieuw_boek[0]}"]

    print(i+1, min_rekken(boeken, rekken))
