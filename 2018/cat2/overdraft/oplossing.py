aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    saldo = int(input())
    regel = input().split(" ")
    regel.pop(0)

    regel = [int(i) for i in regel]
    regel.sort(reverse=True)

    while len(regel) != 0:
        saldo += regel.pop()
        if saldo < 0:
            saldo -= 35
    print(f"{i+1} {saldo}")
        
