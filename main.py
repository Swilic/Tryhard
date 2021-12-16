from openpyxl import *

# Charge le document
wb = load_workbook(filename="Note.xlsx")
sheet = wb.active
# Nom des cours sur la première ligne. AO, FR, Prog, Sys Expl, GBDD
# Total sur la ligne 20 -- G
# Acquis/ Non acquis sur la ligne 21 -- G
note = input("Entrez la note: ")
note = note.split("/")
note_sur_vingt = int(note[0]) / int(note[1]) * 20

# Cherche une case vide pour le FR || Modifier pour user choisi
fr, a, b = "B2", 2, 0
while sheet[fr].value is not None:
	fr = "B" + str(a)
	a += 1
# Ecrit la note/20 sur un emplacement libre
sheet[fr] = note_sur_vingt


wb.save(filename="Note.xlsx")
