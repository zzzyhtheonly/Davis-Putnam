import sys

f = open(sys.argv[1], "r")

# input
line = f.readline()
tmp = line.split()
cnt = 0
start = []
cnt = int(len(tmp) / 2) + 1
for i in range(1,len(tmp),2):
	start.append(tmp[i])

line = f.readline()
tmp = line.split()
end = [-1] * cnt
for i in range(0,len(tmp),2):
	end[int(tmp[i])] = tmp[i + 1]
end.pop(0)

line = f.readline()
tmp = line.split()
ddl = int(tmp[0])

f.close()

vals = []
for i in range(0,len(start)):
	if start[i] not in vals:
		vals.append(start[i])

# define Atoms
atoms = [0]
val_end = 0
for i in range(0,ddl + 1):
	for j in range(1,cnt):
		for k in vals:
			atoms.append((j,k,i))
			val_end += 1
assign_end = val_end
for i in range(0,ddl):
	for j in range(1,cnt):
		for k in range(1,cnt):
			if j != k:
				atoms.append((j,k,i))
				assign_end += 1

# define Axiom
clauses = []

# Unique values
for i in range(0,ddl + 1):
	for j in vals:
		for k in range(1,cnt):
			idx = atoms.index((k,j,i))
			for vb in vals:
				if j != vb:
					clauses.append([-idx,-atoms.index((k,vb,i))])

#Positive Effects of Actions Axiom
for i in range(0,ddl):
	for j in vals:
		for ra in range(1,cnt):
			idx = atoms.index((ra,j,i + 1))
			for rb in range(1,cnt):
				if ra != rb:
					clauses.append([-atoms.index((ra,rb,i)),-atoms.index((rb,j,i)),idx])

#Frame Axiom
for i in range(0,ddl):
	for j in range(1,cnt):
		for k in vals:
			tmp = [-atoms.index((j,k,i)),atoms.index((j,k,i + 1))]
			for rb in range(1,cnt):
				if j != rb:
					tmp.append(atoms.index((j,rb,i)))
			clauses.append(tmp)

#Incompatible Assignment Axiom
for i in range(0,ddl):
	for ra in range(1,cnt):
		for rb in range(1,cnt):
			for rc in range(1,cnt):
				if ra != rb and rb != rc and ra != rc:
					clauses.append([-atoms.index((ra,rb,i)),-atoms.index((rb,ra,i))])
					clauses.append([-atoms.index((ra,rb,i)),-atoms.index((ra,rc,i))])
					clauses.append([-atoms.index((ra,rb,i)),-atoms.index((rb,rc,i))])

# Startings
for i in range(1,cnt):
	clauses.append([atoms.index((i,start[i - 1],0))])
# Goals
for i in range(1,cnt):
	if end[i - 1] != -1:
		clauses.append([atoms.index((i,end[i - 1],ddl))])
		
	

f = open('tmpinputforDP',"w")
s = ""
for i in clauses:
	for j in range(len(i) - 1):
		s = s + str(i[j]) + " "
	s = s + str(i[len(i) - 1]) + "\n"

s = s + "0" + "\n"
#s = str(val_end) + " " + str(assign_end) + " " + str(ddl) + "\n"
for i in range(1,len(atoms)):
	s = s + str(i)
	for j in range(len(atoms[i]) - 1):
		s = s + " " + str(atoms[i][j])
	s = s + " " + str(atoms[i][len(atoms[i]) - 1]) + "\n"

f.write(s)
f.close()


		

