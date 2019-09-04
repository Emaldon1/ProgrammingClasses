Chrom = {}

with open("SV_eqtls_100.txt","r") as Chromosomes:
	for line in Chromosomes.readlines():
		line=line.rstrip()
		items=line.split("\t")
		SV=items[0]
		genes=items[1]
		if SV in Chrom:
			Chrom[SV].append(genes)
		else:
			Chrom[SV]=[genes]

with open("SV_positions.txt","r") as Positions:
	for line in Positions.readlines():
		line=line.rstrip()
		items=line.split("\t")
		SV=items[0]
		if SV in Chrom.keys():
			print(Chrom[SV])
	
