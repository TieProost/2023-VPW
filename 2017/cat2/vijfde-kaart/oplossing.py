t = int(input())
# t = 1
letters = {'B': 11, 'V': 12, 'H': 13, 'A': 1}
soorten = ['K', 'R', 'H', 'S']


def sort_key(tup):
    return (tup[0], tup[1])


for i in range(t):
    kaarten = input().split(" ")
    # kaarten = ["S7", "HV", "K8", "R3"]
    # kaarten = ["HB", "KV", "R2", "H2"]
    # kaarten = ["S10", "K2", "R3", "H9"]
    # kaarten = ["S9", "K10", "H9", "S10"]

    tokens = []

    if kaarten[0][1] in letters:
        eerste = letters[kaarten[0][1:]]
    else:
        eerste = int(kaarten[0][1:])

    for j in range(3):
        nummer = kaarten[j+1][1:]
        if nummer in letters:
            tokens.append((letters[nummer], soorten.index(kaarten[j+1][0])))
        else:
            tokens.append((int(nummer), soorten.index(kaarten[j+1][0])))

    tokensUnSorted = tokens.copy()
    tokensSorted = sorted(tokens, key=sort_key)

    # print(eerste)

    # laagste
    if tokensSorted.index(tokensUnSorted[0]) == 0:
        # middelste hoogste
        if tokensSorted.index(tokensUnSorted[1]) == 1:
            nummer = (eerste + 1) % 13
            # print("dir 1")
        # hoogste middelste
        else:
            nummer = (eerste + 2) % 13
            # print("dir 2")
    # middelste
    elif tokensSorted.index(tokensUnSorted[0]) == 1:
        # laagste hoogste
        if tokensSorted.index(tokensUnSorted[1]) == 0:
            nummer = (eerste + 3) % 13
            # print("dir 3")
        # hoogste laagste
        else:
            nummer = (eerste + 4) % 13
            # print("dir 4")
    # hoogste
    else:
        # laagste middelste
        if tokensSorted.index(tokensUnSorted[1]) == 0:
            nummer = (eerste + 5) % 13
            # print("dir 5")
        # middelste laagste
        else:
            nummer = (eerste + 6) % 13
            # print("dir 6")

    # einde print
    if nummer in [11, 12, 13, 1]:
        for k, v in letters.items():
            if v == nummer:
                nummer = k
    if nummer == 0:
        nummer = 'H'

    print("{} {}{}".format(str(i+1), kaarten[0][0], str(nummer)))
