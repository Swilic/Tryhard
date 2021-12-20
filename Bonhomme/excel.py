from openpyxl import load_workbook

path = "C:\\Users\\diama\\OneDrive\\TEP 1\\Note.xlsx"
# Charge le document
wb = load_workbook(path)
sheet = wb.active

# Demande le cours et crée une variable pour la nommée + variable numéro colonne.
cours = input("Quel cours: AO, FR, PY, SYS, GBD? ").lower()
col_cours = 0
if cours == "ao":
	cours = "A"
	col_cours = 1
elif cours == "fr":
	cours = "B"
	col_cours = 2
elif cours == "py":
	cours = "C"
	col_cours = 3
elif cours == "sys":
	cours = "D"
	col_cours = 4
elif cours == "gdb":
	cours = "E"
	col_cours = 5
else:
	print("Pas valide!")

# Créer boucle pour demander note plusieurs fois.
Continuer = True
while Continuer:
	# Nom des cours sur la première ligne. AO, FR, Prog, Sys Expl, GBDD
	# Total sur la ligne 20 -- G
	# Acquis/ Non acquis sur la ligne 21 -- G
	note = input("Q pour quitter"+"\nEntrez la note: ")
	# stop tout si user demande de quiter
	if note.lower() == "q":
		break
	else:
		pass
	note = note.split("/")
	note_sur_vingt = int(note[0]) / int(note[1]) * 20

	# Cherche une case vide pour le FR
	a = 2
	colonne = cours + str(a)
	while sheet[colonne].value is not None:
		a += 1
		colonne = cours + str(a)
	# Ecrit la note/20 sur un emplacement libre
	sheet[colonne] = note_sur_vingt

	# Fais la somme de chaque valeur dans la colonne.
	somme = 0
	for i in sheet.iter_rows(min_row=2, max_row=a, min_col=col_cours, max_col=col_cours):
		somme += i[0].value * 5

	# Ecrit la moyenne en bas de la colonne.
	sheet[cours+"20"] = somme / (a-1)

	wb.save(path)
