def zoekPatroon(slinger):
    begin = huidig = slinger.index("*")
    interval = 0

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
    eersteIndexPatroon = slinger.index(patroon)

    start = ""
    if eersteIndexPatroon != 0:
        start = patroon[len(patroon) - eersteIndexPatroon:]

    aantalKeer = (len(slinger) - len(start)) // len(patroon)
    res = start + (patroon * aantalKeer)
    aantalCharactersEinde = len(slinger) - len(res)
    res += patroon[:aantalCharactersEinde]

    return res


aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    lengte = int(input())
    slinger = input()
    correct = corrigeer(slinger)
    print(f"{i+1} {correct}")
