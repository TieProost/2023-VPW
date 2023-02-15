lijsten = []
for i in range(int(input())):
    lijst = []
    for j in range(int(input())):
        lijst.append(int(input()))
    lijsten.append(lijst)

for i, v in enumerate(lijsten):
    print(i + 1, min(v), max(v))