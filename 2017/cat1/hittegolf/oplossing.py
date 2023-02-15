def hittegolf(testgeval):
    if len(testgeval) < 5:
        return "geen hittegolf"
    reeks25 = 0
    reeks30 = 0
    hittegolf = False
    for i, temp in enumerate(testgeval):
        if temp >= 25.0:
            reeks25 += 1
            if temp >= 30.0:
                reeks30 += 1
        else:
            if hittegolf == True:
                return f"{start+1} {i-start}"
            reeks25 = 0
            reeks30 = 0

        if reeks25 >= 5 and reeks30 >= 3:
            hittegolf = True
            start = i - reeks25 + 1
    if hittegolf == True:
        return f"{start} {i}"
    return "geen hittegolf"


for i in range(int(input())):
    testgeval = []
    regel = input()
    while regel != "stop":
        testgeval += [float(regel)]
        regel = input()
    print(i+1, hittegolf(testgeval))
