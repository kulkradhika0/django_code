
with open("views.py") as fp:
	for i,line in enumerate(fp):
		if "\Xe2" in line:
			print i,repr(line)
