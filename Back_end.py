import sys

f = open('tmpinputforBack',"r")

l = []
T_sol = []
atoms = []
tag = True
for line in f.readlines():
	if line == "No solution":
		print("No solution")
		exit()
	tmp = line.split()
	if tmp[0] == '0':
		tag = False
		continue
	for i in tmp:
		l.append(i)
	if tag and l[1] == 'T':
		T_sol.append(int(l[0]))
	if tag == False:
		atoms.append(l[1:4].copy())
	l.clear()
f.close()

prev = 0
s = ""
judge = True
tag = True
for i in T_sol:
	if judge and int(atoms[i - 1][2]) < prev:
		judge = False
		prev = 0
	elif judge:
		prev = int(atoms[i - 1][2])
		continue
	if tag:
		s = s + "Cycle" + " " + str(int(atoms[i - 1][2]) + 1) + ": " + "R" + str(atoms[i - 1][0]) + " = " + "R" + str(atoms[i - 1][1])
		prev = atoms[i - 1][2]
		tag = False
	elif prev != atoms[i - 1][2]:
		s = s + "." + "\n" + "Cycle" + " " + str(int(atoms[i - 1][2]) + 1) + ": " + "R" + str(atoms[i - 1][0]) + " = " + "R" + str(atoms[i - 1][1])
		prev = atoms[i - 1][2]
	else:
		s = s + "; " + "R" + str(atoms[i - 1][0]) + " = " + "R" + str(atoms[i - 1][1])
s += "."
print(s)