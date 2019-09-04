print('Erika','Maldonado-Rosado','emaldon1@uncc.edu')

class GeneExpression:
    InstanceCount = 0
    
    @classmethod
    def IncrementCount(self):
        self.InstanceCount +=1
    
    def __init__(self,hwfile):
        self.number = self.InstanceCount
        self.IncrementCount()                

hwfile1 = '/Users/erika/OneDrive/Desktop/TCGA-01R-geneExpression.txt'
hwfile2 = '/Users/erika/OneDrive/Desktop/TCGA-02R-geneExpression.txt'
GE = GeneExpression(hwfile1)
GH = GeneExpression(hwfile2)
print(GE.InstanceCount)
print(GH.InstanceCount)
