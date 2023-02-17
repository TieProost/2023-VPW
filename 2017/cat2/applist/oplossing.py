aantalTestGevallen = int(input())
for i in range(aantalTestGevallen):
    getallen = [int(i) for i in input().split(" ")]
    aantalAppsPerScherm = getallen[0]

    config = [int(i) for i in input().split(" ")]
    oproepen = [int(i) for i in input().split(" ")]

    aantalVeegBewegingen = 0
    for oproep in oproepen:
        index = config.index(oproep)
        if index != 0:
            config[index], config[index-1] = config[index-1], config[index]
            aantalVeegBewegingen += index // aantalAppsPerScherm
    print(f"{i+1} {aantalVeegBewegingen}")