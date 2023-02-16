def zoekPatroon(slinger):
    index = slinger.index("*")
    i = index
    interval = 0
    index += 1
    dic = {}
    while (3 not in dic.values()):
        while (index < len(slinger) and slinger[index] != "*"):
            index += 1
        interval = index - i
        if str(interval) in dic.keys():
            dic[str(interval)] += 1
        else:
            dic[str(interval)] = 1
        i = index
        index += 1

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