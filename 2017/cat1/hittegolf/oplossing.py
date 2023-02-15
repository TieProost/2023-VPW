def hittegolf(testgeval):
    reeks25 = 0
    reeks30 = 0

    for i, temp in enumerate(testgeval):

        if temp >= 25.0:
            reeks25 += 1

            if temp >= 30.0:
                reeks30 += 1

        else:
            if reeks25 >= 5 and reeks30 >= 3:
                start = i + 1 - reeks25
                return f"{start} {i + 1 - start}"  # hittegolf

            reeks25 = 0
            reeks30 = 0

    return "geen hittegolf"


for i in range(int(input())):
    testgeval = []
    regel = input()
    while regel != "stop":
        testgeval += [float(regel)]
        regel = input()

    print(i+1, hittegolf(testgeval))
