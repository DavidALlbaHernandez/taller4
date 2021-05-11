#Cuente e imprima cuantas ciudades inician con la latra M  
archivo = open('paises.txt', 'r')
print("las ciudades que inician con la letra M son: ")
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
	if(i[0]=="M"):
		print(i)
		lista.append(i)
print(len(lista))
archivo.close()
