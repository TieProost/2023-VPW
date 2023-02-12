import subprocess
import sys

opgave = "2018/cat2/fracking" if len(sys.argv) == 1 else sys.argv[1]

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

expected = open(wedstrijd_uitvoer, "r")
resultaat = open(oplossing_uitvoer, "r")

juist = 0
for i, line in enumerate(expected.readlines()):
    if line == resultaat.readline():
        juist += 1

# print resultaat

percentage = int((juist/(i+1))*100)
print(f"\n{opgave}")
print(f"\n{opgave}\n{percentage}% = {150 if percentage == 100 else percentage} punten\n")
