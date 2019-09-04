import pandas as pd

print('Erika','Maldonado-Rosado','emaldon1@uncc.edu')

class geneExpressionTCGA:
    
    def __init__(self,file):
        self.file = file
        self.df = self.readfiles()
        #self.genes = Genes
        #self.values = self.get_values()
        #self.colname = "TCGA"
        # self.newdf = self.exp_difference()
        #print (self.values)
        
    def readfiles(self):
        df = pd.read_csv(self.file, sep = '\t', names =["Genes", "Expression"], index_col = "Genes")
        print (df)
        
    def get_values(self):
        exp = (self.df.loc[self.df['Genes'] == self.genes])
        return exp
        
    def exp_diff(self,second_file,second_gene):
        new_data = geneExpressionTCGA(second_file,second_gene)
        newdf = new_data.df.merge(self.df, on = 'Genes')
        names = ['Genenames',self.colname,new_data.colname ]
        newdf['Difference'] = newdf[self.colname+"_x"] - newdf[new_data.colname+"_y"]
        print(newdf)
        
TCGA_2670 = '/Users/erika/OneDrive/Desktop/hw4-TCGA/hw4-TCGA/TCGA-A6-2670-01A-02R-0821-07-geneExpression.txt'
TCGA_2683 = '/Users/erika/OneDrive/Desktop/hw4-TCGA/hw4-TCGA/TCGA-A6-2683-01A-01R-0821-07-geneExpression.txt'    
g1 = geneExpressionTCGA(TCGA_2670)
print(g1)

g2 = geneExpressionTCGA(TCGA_2683)
print(g2)

