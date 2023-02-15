for i in range(int(input())):

    dimensies = input().split(" ")

    rijen = int(dimensies[0])
    kolommen = int(dimensies[1])
    array = [["." for _ in range(kolommen)] for _ in range(rijen)]

    kruisptn = input().split(" ")

    for j in range(int(kruisptn[0])):
        kruispunt_x = int(kruisptn[j*2+1]) - 1
        kruispunt_y = int(kruisptn[j*2+2]) - 1
        array[kruispunt_x][kruispunt_y] = "*"

        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            punt_x = kruispunt_x + x
            punt_y = kruispunt_y + y

            while -1 < punt_x < len(array) and -1 < punt_y < len(array[0]):
                if array[punt_x][punt_y] != "*":
                    array[punt_x][punt_y] = "*"
                else:
                    break
                punt_x += x
                punt_y += y

    for k in range(rijen):
        print(i+1, "".join(array[k]))
