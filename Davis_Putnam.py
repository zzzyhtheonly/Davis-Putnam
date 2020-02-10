import sys
import copy

f = open('tmpinputforDP', "r")

# input clauses
g_clauses = []
# input relationship
rel = {}
# var used for counting pure literal
g_pure = {}
# solution
sol = {}

# fill input data structure
tag = True
for line in f.readlines():
	str1 = line.split()
	if str1[0] == '0':
		tag = False
		continue
	t_clause = []
	for i in str1:
		if tag:
			t_clause.append(int(i))
			if i not in g_pure.keys():
				g_pure[int(i)] = 1
			else:
				g_pure[int(i)] += 1
		else:
		    t_clause.append(i)
	if tag:
		g_clauses.append(t_clause)
	elif tag != True:
		rel[t_clause[0]] = t_clause[1:4].copy()

# Davis-Putnam
def DP(clauses,pure,sol):
	if len(clauses) == 0:
		return True
	# check singleton
	for i in range(len(clauses)):
		if len(clauses[i]) == 1:
			val = clauses[i][0]
			rev = 0 - val
			# add to the solution
			if val > 0:
				sol[val] = "T"
			else:
				sol[rev] = "F"
			# delete clauses
			for j in range(len(clauses)):
				if clauses[j].count(rev) != 0:
					if len(clauses[j]) == 1:
						return False
					clauses[j].remove(rev)
			for j in range(len(clauses)):
				if clauses[j].count(val) != 0:
					clauses[j] = 0
			for j in range(clauses.count(0)):
				clauses.remove(0)
			# delete counting
			if val in pure.keys():
				del pure[val]
			if rev in pure.keys():
				del pure[rev]
			# next
			return DP(copy.deepcopy(clauses),copy.deepcopy(pure),sol)
			
	# check pure literal
	for i in range(len(clauses)):
		for j in range(len(clauses[i])):
			val = clauses[i][j]
			rev = 0 - val
			t_clauses = clauses.copy()
			t_sol = sol.copy()
			t_pure = pure.copy()
			if rev not in pure.keys():
				if val > 0:
					sol[val] = "T"
				else:
					sol[rev] = "F"
				for k in range(len(clauses)):
					if clauses[k].count(val) != 0:
						clauses[k] = 0
				for k in range(clauses.count(0)):
					clauses.remove(0)
				del pure[val]
				return DP(copy.deepcopy(clauses),copy.deepcopy(pure),sol)

	# the try process
	t_clauses = copy.deepcopy(clauses)
	t_pure = copy.deepcopy(pure)
	tag = True
	
	val = clauses[0][0]
	rev = 0 - val
	if val > 0:
		sol[val] = "T"
	else:
		sol[rev] = "F"
	# delete clauses
	for j in range(len(clauses)):
		if clauses[j].count(rev) != 0:
			if len(clauses[j]) == 1:
				tag = False
			clauses[j].remove(rev)
	for j in range(len(clauses)):
		if clauses[j].count(val) != 0:
			clauses[j] = 0
	for j in range(clauses.count(0)):
		clauses.remove(0)
	# delete counting
	if val in pure.keys():
		del pure[val]
	if rev in pure.keys():
		del pure[rev]
	# judge
	if tag:
		tag = DP(copy.deepcopy(clauses),copy.deepcopy(pure),sol)
	if tag:
		return True
	# retry
	clauses = copy.deepcopy(t_clauses)
	pure = copy.deepcopy(t_pure)
	tag = True
	
	val = 0 - clauses[0][0]
	rev = 0 - val
	if val > 0:
		sol[val] = "T"
	else:
		sol[rev] = "F"
	# delete clauses
	for j in range(len(clauses)):
		if clauses[j].count(rev) != 0:
			if len(clauses[j]) == 1:
				tag = False
			clauses[j].remove(rev)
	for j in range(len(clauses)):
		if clauses[j].count(val) != 0:
			clauses[j] = 0
	for j in range(clauses.count(0)):
		clauses.remove(0)
	# delete counting
	if val in pure.keys():
		del pure[val]
	if rev in pure.keys():
		del pure[rev]
	# judge
	if tag:
		tag = DP(copy.deepcopy(clauses),copy.deepcopy(pure),sol)
	if tag:
		return True
	clauses = t_clauses
	sol = t_sol
	pure = t_pure
	return False

# main
s = ""
if DP(copy.deepcopy(g_clauses),copy.deepcopy(g_pure),sol):
	out = sorted(sol.keys())
	for i in out:
		s = s + str(i) + " " + sol[i] + "\n"
	
	s = s + "0" + "\n"
	for i in rel.keys():
		s = s + str(i)
		for j in rel[i]:
			s = s + " " + str(j)
		s = s + "\n"
	
else:
	s += "No solution"
f = open('tmpinputforBack',"w")
f.write(s)
f.close()