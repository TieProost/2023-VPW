import math

def zoekPatroon(slinger):
    aantalDots = lengteSlinger // 5

    for aantal in range(aantalDots,0,-1):
        if slinger.count("." * aantal) >= 3:
            return "*" + "." * aantal

def corrigeer(slinger):
    patroon = zoekPatroon(slinger)
    eersteIndex = slinger.index(patroon)

    start = patroon[len(patroon) - eersteIndex:]
    aantalKeer = math.ceil(lengteSlinger / len(patroon))
    res = start + (patroon * aantalKeer)

    return res[:lengteSlinger]

aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    lengteSlinger = int(input())
    slinger = input()
    correct = corrigeer(slinger)
    print(f"{i+1} {correct}")
