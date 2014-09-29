import csv
import numpy

def leerMatriz():
	reader=csv.reader(open('montanteDatos.csv','rb'),delimiter=',')
	listR=list(reader)
	matriz=numpy.array(listR).astype('int')
	return matriz

matriz = leerMatriz()	
print "Matriz Inicial\n" + str(matriz)

# piv es pivote
# r es row
# c es col
pivAnt = 1
for pivN in range(0,3):
	for r in range(0,3):
		for c in range(0,4):
			if c != pivN and r!= pivN:
				matriz[r][c]=(matriz[pivN][pivN] * matriz[r][c] -matriz[r][pivN]*matriz[pivN][c])/pivAnt
		if r != pivN:
			matriz[r][pivN]	= 0
	print "\n" + str(matriz)
	pivAnt=matriz[pivN][pivN]

print 
print "Matriz final\n\n" + str(matriz)	

x=matriz[0][0]/matriz[0][3]
y=matriz[1][1]/matriz[1][3]
z=matriz[2][2]/matriz[2][3]


print "\nValores de x,y,z:" 
print "X = " + str(x)
print "Y = " + str(y)
print "Z = " + str(z)

