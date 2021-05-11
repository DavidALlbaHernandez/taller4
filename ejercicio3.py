#Cuente e imprima cuantos paises que hay en el archivo
archivo = open('paises.txt', 'r')
P=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  P=P+1 
  if(a=="Paises\n"):
    break
  lista=[]   
print(" la cantidad de paises en el archivo es: "+str(P))
archivo.close()