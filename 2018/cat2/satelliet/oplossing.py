def decode(scan, signaalNaarLetter):
    sortedKeys = sorted(signaalNaarLetter.keys(), key=lambda x: len(x), reverse=True)
    orderedDict = {key: signaalNaarLetter[key] for key in sortedKeys}
    decoded = ""
    while len(scan) != 0:
        replaced = False
        for key in orderedDict.keys():
            if scan.startswith(key):
                decoded += orderedDict[key]
                scan = scan.replace(key, "",1)
                replaced = True
                break
        if replaced is False:
            return "ONMOGELIJK"
    return decoded
           
aantalTestGevallen = int(input())

for i in range(aantalTestGevallen):
    scan = input()
    aantalLetterCodes = int(input())
    signaalNaarLetter = dict()

    for _ in range(aantalLetterCodes):
        letter = input()
        code = input()
        signaalNaarLetter[code] = letter
    decoded = decode(scan, signaalNaarLetter)
    print(f"{i+1} {decoded}")
    