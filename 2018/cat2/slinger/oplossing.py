import math


def zoekPatroon(slinger):
    begin = huidig = slinger.index("*")

    dic = {}
    while (3 not in dic.values()):

        huidig += 1
        while (huidig < len(slinger) and slinger[huidig] != "*"):
            huidig += 1

        interval = huidig - begin
        begin = huidig

        dic[interval] = dic[interval] + 1 if interval in dic else 1

    return "*" + "."*(interval-1)


def corrigeer(slinger):
    patroon = zoekPatroon(slinger)
    eersteIndex = slinger.index(patroon)

    start = ""
    if eersteIndex != 0:
        start = patroon[len(patroon) - eersteIndex:]

    aantalKeer = math.ceil(len(slinger) / len(patroon))
    res = start + (patroon * aantalKeer)

    return res[:len(slinger)]


aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    lengte = int(input())
    slinger = input()
    correct = corrigeer(slinger)
    print(f"{i+1} {correct}")
