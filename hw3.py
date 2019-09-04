import sys
from re import match, search
print('Erika','Maldonado-Rosado','emaldon1@uncc.edu')
class GeneBankEntry():
    def __init__(self,infile):
        self.genDic = {}
        C = ' '
        #gcContent = ' '
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
                elif search('\s*\d[^0-9]',line): #starting to parse through the data. Had trouble bc it displayed number=. Tried to take it out but it did not work.
                    C +=line.strip()                 
                    C = ''.join([i for i in C if not i.isdigit()]) #taking out digits
                    C = C.replace(" ","")[11:] #removing spaces
                    (self.genDic['ORIGIN']) = C       #Assigning my dictionary to C                                                
                                      
    def __str__(self):
        return '[Organism]'+self.genDic['Organism']
        
    def display(self):
        print (self.genDic)
        
    def is_motif(self,motif):
        if motif in self.genDic['ORIGIN']:
            return 'Motif:' +motif +' ' + 'sequence is in the dictionary' #if motif is here please tell me its in the dictionary
        else:
            return 'Motif:' +motif + ' ' + 'sequence was not found in the dictionary'#if motif is not found tell me it is in here
            
    def gc_Content(self):
        g = self.genDic['ORIGIN'].count('g')
        c = self.genDic['ORIGIN'].count('c')
        percentgc =((g+c)/len(self.genDic['ORIGIN']))*100
        gcContent ="%.2f"% round(percentgc,2)
        return gcContent
       
    
hwfile = "/Users/erika/OneDrive/Desktop/hw2_hla.gb.txt" #bringing in file
foo=GeneBankEntry(hwfile)
print (str(foo))
foo.display()
print (foo.is_motif('acg'))
print (foo.is_motif('cgc'))
print (foo.gc_Content())