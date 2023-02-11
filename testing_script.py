import subprocess

opgave = "2018/cat2/fracking"
wedstrijd_invoer = opgave + "/wedstrijd.invoer"
wedstrijd_uitvoer = opgave + "/wedstrijd.uitvoer"
oplossing_script = opgave + "/oplossing.py"
oplossing_uitvoer = opgave + "/oplossing.uitvoer"


# schrijf oplossing.uitvoer

stdin = open(wedstrijd_invoer, "r")
stdout = open(oplossing_uitvoer, "a")
stdout.seek(0)
stdout.truncate()

subprocess.Popen(f"python {oplossing_script}",
                 stdin=stdin, stdout=stdout).communicate()

# bereken punten

juist = totaal = 0
expected = open(wedstrijd_uitvoer, "r")
oplossing = open(oplossing_uitvoer, "r")

for line in expected.readlines():
    if oplossing.readline() == line:
        juist += 1
    totaal += 1

percentage = int((juist/totaal)*100)
print(f"\n{percentage}% = {150 if percentage == 100 else percentage} punten\n")
