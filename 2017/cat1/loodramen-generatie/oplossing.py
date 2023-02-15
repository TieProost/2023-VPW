for i in range(int(input())):

    rijen_kolommen = input().split(" ")
    rijen = int(rijen_kolommen[0])
    kolommen = int(rijen_kolommen[1])

    array = [["." for i in range(kolommen)] for i in range(rijen)]

    kruispunten = []
    regel = input().split(" ")
    for j in range(0, int(regel[0])*2, 2):

        kruispunt_x = int(regel[j+1]) - 1
        kruispunt_y = int(regel[j+2]) - 1
        array[kruispunt_x][kruispunt_y] = "*"

        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            punt_x = kruispunt_x + x
            punt_y = kruispunt_y + y

            while -1 < punt_x < len(array) and -1 < punt_y < len(array[0]):
                if array[punt_x][punt_y] != "*":
                    array[punt_x][punt_y] = "*"
                elif array[punt_x][punt_y] == "*":
                    break

                punt_x += x
                punt_y += y

    for k in range(rijen):
        print(i+1, "".join(array[k]))
