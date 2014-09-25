import csv
import numpy

def leerMatriz():
	reader=csv.reader(open('montanteDatos.csv','rb'),delimiter=',')
	x=list(reader)
	matrixAct=numpy.array(x).astype('float')
	return matrixAct

def CerosCol1(matrixAct):
	for pivoteCol in range(1,4):
		matrixAct[pivoteCol][0] = 0
	return matrixAct


matrixAct = leerMatriz()
matrixAnt = matrixAct
matrixAct = CerosCol1(matrixAct)	

print matrixAnt
print matrixAct

pivote = matrixAct[0][0]

for element in matrixAnt:
	print element
	