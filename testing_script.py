import subprocess

opgave = "2018/cat2/fracking"

# schrijf oplossing.uitvoer

stdin = open(opgave + "/wedstrijd.invoer", "r")
stdout = open(opgave + "/oplossing.uitvoer", "a")
stdout.seek(0)
stdout.truncate()

subprocess.Popen(f"python {opgave}/oplossing.py",
                 stdin=stdin, stdout=stdout).communicate()

# bereken punten

juist = totaal = 0
expected = open(opgave+"/wedstrijd.uitvoer", "r")
oplossing = open(opgave+"/oplossing.uitvoer", "r")

for line in expected.readlines():
    if oplossing.readline() == line:
        juist += 1
    totaal += 1

percentage = int((juist/totaal)*100)
print(f"{percentage}% = {150 if percentage == 100 else percentage} punten")
