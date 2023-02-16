def ontbrekendGetal(getal):
    length_found = False
    length = 1
    ontbreekt = -1
    while not length_found:
        index = 0
        test = True
        tmplength = length
        while index+tmplength < len(getal) and test:
            tmp = int(getal[index:index+tmplength])+1
            tmplengte = len(str(tmp))
            einde = index+2*tmplength if tmplengte == tmplength else index+2*tmplength+1
            tmp2 = int(getal[index+tmplength:einde])
            if tmp > tmp2:
                tmp2 = int(getal[index+tmplength:einde+1])
                tmplengte += 1
            if not (tmp == tmp2 or tmp+1 == tmp2):
                test = False
            if tmp+1 == tmp2:
                if ontbreekt == -1:
                    ontbreekt = tmp
                else:
                    test = False
            index += tmplength
            if tmplengte > tmplength:
                tmplength = tmplengte
        length_found = test
        if not length_found:
            ontbreekt = -1
        length += 1
    return "geen ontbrekend getal" if ontbreekt == -1 else f"{ontbreekt}"


t = int(input())
for i in range(1, t+1):
    print(f"{i} {ontbrekendGetal(input())}")
