print('Erika','Maldonado-Rosado','emaldon1@uncc.edu')
class GeneBankEntry():
    def __init__(self,infile):
        self.genkey = ['Accession','GI','Organism','gene']
        self.genDic = {key: None for key in self.genkey}

        with open(infile, "r") as gb:
            for line in gb.readlines():
                if line.startswith('ACCESSION'):
                    self.genDic ['Accession'] = line.rstrip('\n').split('  ')[1]
                    a = ''.join(self.genDic['Accession'])
                    a.strip()
                    self.genDic['Accession'] = a
                elif line.startswith('VERSION'):
                    b = (line.rstrip('\n').split() [2])
                    self.genDic['GI'] = b.split('GI:')[1]
                    
                elif 'ORGANISM' in line:
                    line_org = line.strip().rstrip('\n').split()
                    value_org = line_org[1]+" "+line_org[2]
                    self.genDic['Organism'] = value_org
                    
                elif '/gene' in line:
                            Row = line.rstrip('\n').split('=')[1].strip('\"')
                            self.genDic['gene'] = Row
    
    def __str__(self):
        return '[Organism]'+self.genDic['Organism']
        
    def display(self):
        print (self.genDic)
    
    
            
# I run at run time!    
hwfile = "/Users/erika/OneDrive/Desktop/hw2_hla.gb.txt" #bringing in file
#print(hwfile.name)
foo=GeneBankEntry(hwfile)
print (str(foo))
foo.display()