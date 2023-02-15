def hittegolf(testgeval):

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
                return f"{start_index+1} {lengte}"

            reeks25 = 0
            reeks30 = 0

        if reeks25 >= 5 and reeks30 >= 3:
            hittegolf = True
            start_index = i + 1 - reeks25
            lengte = i + 1 - start_index

    if hittegolf == True:  # deze if wordt niet bereikt met de gegeven test invoer
        return f"{start_index+1} {lengte}"

    return "geen hittegolf"


for i in range(int(input())):
    testgeval = []
    regel = input()
    while regel != "stop":
        testgeval += [float(regel)]
        regel = input()

    print(i+1, hittegolf(testgeval))
